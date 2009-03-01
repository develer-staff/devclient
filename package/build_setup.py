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

from glob import glob
from os import environ
from os.path import join, exists, basename
from subprocess import call
from shutil import copyfile


packages = ('../src/start.exe',
            '../src/devclient/startcore.exe',
            '../src/update/startupdater.exe')

def checkPackages():
    for p in packages:
        if not exists(p):
            return False
    return True


if __name__ == '__main__':
    if not checkPackages():
        call(['python', 'build_packages.py'])
        for p in packages:
            copyfile(join('dist', basename(p)), p)

    inno_setup = join(environ['INNOSETUP_PATH'], 'ISCC.exe')
    retcode = call([inno_setup, 'devclient.iss'])

