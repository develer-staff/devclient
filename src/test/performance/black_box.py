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

__version__ = "$Revision$"[11:-2]
__docformat__ = 'restructuredtext'


import random
import subprocess
from time import time
from shutil import copy
from sys import argv, path
from os import getcwd, chdir, unlink
from os.path import basename, abspath, normpath, join, dirname, exists

from PyQt4.QtTest import QTest
from PyQt4.QtCore import QTimer, Qt

path.append(join(dirname(abspath(argv[0])), '../..'))

import devclient.exception as exception
from devclient.engine import terminateProcess, startProcess
from devclient.conf import loadConfiguration, config
from devclient.storage import Storage, adjustSchema

_DEF_CONFIG_FILE = "../../../etc/devclient.cfg"
cfg_file = normpath(join(dirname(abspath(argv[0])), _DEF_CONFIG_FILE))


class StartConnection(object):
    def __init__(self, gui):
        self.f = gui._startConnection

    def __call__(self,*a,**k):
        self.time = time()
        return self.f(*a,**k)


class EndConnection(object):
    def __init__(self, gui):
        self.gui = gui
        self.f = gui.displayWarning

    def __call__(self,*a,**k):
        if self.gui._text['ConnLost'] == unicode(a[1]):
            self.time = time()
            callback()
        return self.f(*a,**k)

def startAction(gui):
    callback.s = gui._startConnection = StartConnection(gui)
    callback.e = gui.displayWarning = EndConnection(gui)
    QTest.mouseClick(gui.button_connect, Qt.LeftButton)

def callback():
    print 'total time:' ,callback.e.time - callback.s.time

def readOptions(dirname):
    if exists(join(dirname, 'options.cfg')):
        fd = open(join(dirname, 'options.cfg'))
        data = [r.split('=') for r in fd.readlines()]
        fd.close()
        return dict([(k.strip(), v.strip()) for k,v in data])
    return {}

def main(cfg_file=cfg_file):

    test = 'test' if len(argv) < 2 else argv[1]
    options = readOptions(test)

    old_dir = getcwd()
    chdir(join(getcwd(), dirname(argv[0]), dirname(cfg_file)))
    cfg_file = join(getcwd(), basename(cfg_file))
    loadConfiguration(cfg_file)
    config['storage']['path'] = abspath('../data/storage/dbtest.sqlite')
    adjustSchema()  #create schema must be before adding the connection
    Storage().addConnection([0, 'localhost', 'localhost', 6666])
    path.append(config['servers']['path'])
    path.append(config['resources']['path'])

    chdir(old_dir)
    if exists(join(test, 'localhost_server.py')):
        copy(join(test, 'localhost_server.py'), config['servers']['path'])

    # this import must stay here, after the appending of resources path to path
    from devclient.gui import Gui

    port = random.randint(2000, 10000)

    p = startProcess(['python',
                      join(config['devclient']['path'], 'core.py'),
                      '--config=%s' % cfg_file,
                      '--port=%d' % port])

    # FIX! To prevent connectionRefused from SocketToGui
    import time
    time.sleep(.5)

    try:
        gui = Gui(port)
        cwd = dirname(argv[0]) if dirname(argv[0]) else None
        cmd = ['python', '-u', 'server_test.py']
        if 'delay' in options:
            cmd.append('-d')
            cmd.append(options['delay'])
        cmd.append(test + '/data.txt')
        gui.p = subprocess.Popen(cmd, stdout=subprocess.PIPE, cwd=cwd)

        try:
            buf = gui.p.stdout.read(6) # read READY\n from stdout
        except IOError:
            time.sleep(.5)

        Gui.startAction = startAction
        QTimer.singleShot(2000, gui.startAction)
        gui.mainLoop()
    except exception.IPCError:
        terminateProcess(p.pid)
    except Exception, e:
        print 'Fatal Exception:', e
        terminateProcess(p.pid)
    finally:
        fn = join(config['servers']['path'], 'localhost_server.py')
        if exists(fn):
            unlink(fn)

if __name__ == '__main__':
    main()