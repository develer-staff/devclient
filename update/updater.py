#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Copyright (C) 2007 Gianni Valdambrini, Develer S.r.l (http://www.develer.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author: Gianni Valdambrini gvaldambrini@develer.com

"""
The module to manage the auto updating of the client.
"""

__version__ = "$Revision$"[11:-2]
__docformat__ = 'restructuredtext'

import sys, time
import tarfile
import subprocess
from filecmp import cmp
from optparse import OptionParser
from socket import setdefaulttimeout
from ConfigParser import SafeConfigParser
from shutil import copyfile, rmtree, copymode
from urllib2 import urlopen, HTTPError, URLError, Request
from os import chdir, walk, getcwd, makedirs, rename, sep, unlink
from os.path import basename, splitext, split, abspath
from os.path import exists, join, normpath, dirname

_SELF_MODULE = basename(__file__)
"""the name of the module itself"""

_SELF_DIR = abspath(dirname(__file__))
"""the directory of the module itself"""

_DEVCLIENT_VERSION_FILE = abspath(join(_SELF_DIR, 'devclient.version'))
"""The file where the updater stores the local version of the devclient"""

_PACKAGES_VERSION_FILE = abspath(join(_SELF_DIR, 'packages.version'))
"""The file where the updater stores the local version of the packages"""

_ROOT_DIR = abspath(join(_SELF_DIR, '..'))
"""the root directory of client"""

_TMP_DIR = abspath(join(_SELF_DIR, 'temp'))
"""temp directory where store data for the update"""

_CONFIG_FILE = join(_SELF_DIR, 'updater.cfg')
"""the configuration file"""

type_str = ('source', 'binaries')[hasattr(sys, 'frozen') and sys.frozen]
_DEVCLIENT_AGENT = "DevClient [%s][%s]" % (sys.platform, type_str)
"""the agent used to perform network requests"""


class UpdaterError(Exception):
    """
    Base class for the exceptions of updater.
    """

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


def checkVersion(online_version, local_version):
    """
    Check the existance of a new version to download.

    :Parameters:
      online_version : str
        the online version available
      local_version : str
        the local version
    """

    print 'online version:', online_version, 'local version:', local_version
    online = map(int, online_version.split('.'))
    local = map(int, local_version.split('.'))
    return online > local

def getOnlineVersion(url):
    """
    Return the online version given an url, or the empty string if errors
    occurred.

    :Parameters:
      url : str
        the url of the file that contains the version.
    """

    setdefaulttimeout(2)

    try:
        req = Request(url, None, {'User-agent': _DEVCLIENT_AGENT})
        u = urlopen(req)
    except HTTPError:
        raise UpdaterError('Unable to download file: %s' % url)
    except URLError:
        raise UpdaterError('Url malformed: %s' % url)
    except IOError:
        raise UpdaterError('Timeout on download file: %s' % url)

    return u.read().strip()

def downloadFile(url, timeout=2):
    """
    Download a file from an url and save in the filesystem.

    :Parameters:
      url : str
        the url of file to download
      timeout : int
        timeout to wait before raising error
    """

    setdefaulttimeout(timeout)
    try:
        req = Request(url, None, {'User-agent': _DEVCLIENT_AGENT})
        u = urlopen(req)
    except HTTPError:
        raise UpdaterError('Unable to download file: %s' % url)
    except URLError:
        raise UpdaterError('Url malformed: %s' % url)
    except IOError:
        raise UpdaterError('Timeout on download file: %s' % url)

    length = int(u.info()['content-length'])
    if length > 524288: # 512 KB

        def format_time(seconds):
            return time.strftime('%H:%M:%S', time.gmtime(seconds))

        print 'download updates of:', int(u.info()['content-length']) / 1024, \
            'Kb '

        bar_length = 20
        chunk = length / 50
        data = ''
        start_time = time.time()
        for i in xrange(50):
            completed = int(i / (50.0 / bar_length))
            missing = bar_length - completed
            elapsed = time.time() - start_time
            if completed:
                eta = format_time(elapsed * bar_length / completed - elapsed)
            else:
                eta = '--:--:--'

            sys.stdout.write("\r[%s%s] %2d%% ETA: %s Time: %s" %
                ('#' * completed, '.' * missing, i * 2, eta, format_time(elapsed)))
            sys.stdout.flush()
            data += u.read(chunk)

        data += u.read()
        sys.stdout.write("\r[%s] %2d%% ETA: %s Time: %s\n" %
            ('#' * bar_length, 100, eta, format_time(time.time() - start_time)))
        sys.stdout.flush()
    else:
        data = u.read()

    filename = basename(url)
    fd = open(filename, 'wb+')
    fd.write(data)
    fd.close()

def uncompressFile(filename):
    """
    Extracting the file's data

    :Parameters:
      filename : str
        the name of the file
    """

    try:
        tar = tarfile.open(filename)
        name = normpath(tar.getnames()[0])
        sep_pos = name.find(sep)
        base_dir = name[:sep_pos] if sep_pos != -1 else name
        tar.extractall()
        tar.close()
    except tarfile.ReadError:
        raise UpdaterError('Archive malformed')
    return base_dir

def replaceOldVersion(root_dir, base_dir, ignore_list):
    """
    Replace the old files of installed client with the new files.

    :Parameters:
        root_dir : str
          the root directory of the tree
        base_dir : str
          the base directory of the new version
        ignore_list : list
          the list of files to skip
    """

    chdir(base_dir)
    for root, dirs, files in walk('.'):
        for f in files:
            source = normpath(join(root, f))
            if source in ignore_list:
                d, f = split(source)
                name, ext = splitext(f)
                dest = join(root_dir, d, name + '_ignore' + ext)
                if exists(dest) and cmp(source, dest):
                    continue
                print 'skip file: %s, save into %s' % (source, dest)
            else:
                dest = join(root_dir, source)
                if exists(dest) and cmp(source, dest):
                    continue

                # FIX: this check should be done from the root dir of client
                if basename(source) == _SELF_MODULE:
                    d, f = split(dest)
                    name, ext = splitext(f)
                    rename(dest, join(d, name + '_old' + ext))
                    print 'replace file: %s (old version backupped)' % source
                else:
                    print '%s file:' % ('add', 'replace')[exists(dest)], source

            if not exists(dirname(dest)):
                print 'create directory:', dirname(dest)
                makedirs(dirname(dest))
            copyfile(source, dest)
            copymode(source, dest)

        # create all the directories in the archive
        for d in dirs:
            if not exists(join(root_dir, root, d)):
                makedirs(join(root_dir, root, d))

def update(archive_name, root_dir, ignore_list):
    """
    Update a source tree, starting from an archive and the root dir of the
    tree.

    :Parameters:
        archive_name : str
          the new tree archive
        root_dir : str
          the root directory of the tree
        ignore_list : list
          the list of files to be skipped
    """

    retvalue = False
    if not exists(_TMP_DIR):
        makedirs(_TMP_DIR)

    try:
        chdir(_TMP_DIR)
        base_dir = uncompressFile(archive_name)
        replaceOldVersion(root_dir, base_dir, ignore_list)
    except UpdaterError, e:
        print 'ERROR:', e
    else:
        retvalue = True
    finally:
        chdir(root_dir)  # change directory is required to remove the temp dir
        rmtree(_TMP_DIR)
    return retvalue

def getDevclientVersion():
    """Read and return the local version of the devclient"""

    try:
        fd = open(_DEVCLIENT_VERSION_FILE)
    except IOError:
        # if no local version is found, force the download of the new version
        return '0.0.00'

    data = fd.read().strip()
    fd.close()
    return data

def getPackagesVersion():
    """Read and return the local version of the packages"""

    try:
        fd = open(_PACKAGES_VERSION_FILE)
    except IOError:
        # if no local version is found, force the download of the new version
        return '0.0.00'

    data = fd.read().strip()
    fd.close()
    return data

def saveDevclientVersion(version):
    """Save the new version of the devclient to disk"""

    fd = open(_DEVCLIENT_VERSION_FILE, 'w+')
    fd.write(version)
    fd.close()

def savePackagesVersion(version):
    """Save the new version of the packages to disk"""

    fd = open(_PACKAGES_VERSION_FILE, 'w+')
    fd.write(version)
    fd.close()

def updateFromNet(config):
    """
    The main function of the update through web. 

    It checks the urls set in the configuration file for a new version, and if 
    exists it downloads the archive and replaces the old version of the files
    with the contents of the archive.
    """

    ignore_list = map(normpath, config['files']['ignore'].split(','))
    devclient_version = getDevclientVersion()
    packages_version = getPackagesVersion()
    updated = False
    retcode = 0

    ## Update the client
    client_ver = getOnlineVersion(config['client']['version'])
    if not client_ver:
        print 'Unknown online version of client, skip'

    if client_ver and checkVersion(client_ver, devclient_version):
        downloadFile(config['client']['url'])
        client = abspath(basename(config['client']['url']))
        if not update(client, _ROOT_DIR, ignore_list):
            print 'Fatal error while updating', config['client']['url']
            retcode = 1
        else:
            updated = True
            saveDevclientVersion(client_ver)
        unlink(client)

    ## Update the packages
    if hasattr(sys, 'frozen') and sys.frozen:
        pack_ver = getOnlineVersion(config['packages']['version'])
        if not pack_ver:
            print 'Unknown online version of the packages, skip'

        if pack_ver and checkVersion(pack_ver, packages_version):
            downloadFile(config['packages']['url'], None)
            packages = abspath(basename(config['packages']['url']))
            if not update(packages, _ROOT_DIR, ignore_list):
                print 'Fatal error while updating', config['packages']['url']
                retcode = 1
            else:
                updated = True
                savePackagesVersion(pack_ver)
            unlink(packages)

    return (retcode, updated)

def updateFromLocal(config):
    """
    The main function of the update using local files. 

    It simply replaces the old version of the files with the contents of the 
    archives (if present).
    """

    updated = False
    retcode = 0
    ignore_list = map(normpath, config['files']['ignore'].split(','))
    client = abspath(basename(config['client']['url']))
    packages = abspath(basename(config['packages']['url']))

    ## Update the client
    if exists(client):
        if not update(client, _ROOT_DIR, ignore_list):
            print 'Fatal error while updating', client
            retcode = 1
        else:
            updated = True

    ## Update the packages
    if hasattr(sys, 'frozen') and sys.frozen:
        if exists(packages):
            if not update(packages, _ROOT_DIR, ignore_list):
                print 'Fatal error while updating', packages
                retcode = 1
            else:
                updated = True

    return (retcode, updated)

def main():
    parser = OptionParser()
    parser.add_option('--source', default='net',
                      help='(local|net) the source used for the updates')

    o, args = parser.parse_args()

    cp = SafeConfigParser()
    cp.read(_CONFIG_FILE)
    config = {}
    for s in cp.sections():
        config[s] = dict(cp.items(s))

    if not int(config['main']['update']):
        print 'Update disabled!'
        return 0

    funcUpdate = updateFromLocal if o.source == 'local' else updateFromNet
    retcode, updated = funcUpdate(config)

    if not retcode and updated:
        print 'Update successfully completed!'
    sys.exit(retcode)

