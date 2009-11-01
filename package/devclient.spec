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


import encodings
encs = set(os.path.splitext(n)[0]
    for n in os.listdir(os.path.dirname(encodings.__file__)))
encs -= set(['__init__', 'aliases', 'utf_8', 'latin_1', 'cp850', 'idna', 'ascii'])

# devclient
dev_an = Analysis([os.path.join(HOMEPATH,'support/_mountzlib.py'),
              os.path.join(HOMEPATH,'support/useUnicode.py'),
              '../devclient.py'],
             pathex=['.', '../src/devclient'],
             excludes=map('encodings.'.__add__, encs))

dev_pyz = PYZ(dev_an.pure - [el for el in dev_an.pure if 'devclient' in el[1]])
dev_exe = EXE(dev_pyz,
              dev_an.scripts,
              dev_an.binaries,
              dev_an.zipfiles,
              name=os.path.join('dist', 'devclient.exe' if sys.platform == 'win32' else 'devclient'),
              debug=False,
              strip=False,
              upx=True,
              console=1,
              icon='develer.ico',
              append_pkg=False)

# startcore
core_an = Analysis([os.path.join(HOMEPATH,'support/_mountzlib.py'),
              os.path.join(HOMEPATH,'support/useUnicode.py'),
              '../src/devclient/startcore.py'],
             pathex=['.'],
             excludes=map('encodings.'.__add__, encs))

core_pyz = PYZ(core_an.pure - [el for el in core_an.pure if 'devclient' in el[1]])
core_exe = EXE(core_pyz,
               core_an.scripts,
               core_an.binaries,
               core_an.zipfiles,
               name=os.path.join('dist', 'startcore.exe' if sys.platform == 'win32' else 'startcore'),
               debug=False,
               strip=False,
               upx=True,
               console=1,
               icon='develer.ico',
               append_pkg=False)

# startupdater
upd_an = Analysis([os.path.join(HOMEPATH,'support/_mountzlib.py'),
              os.path.join(HOMEPATH,'support/useUnicode.py'),
              '../update/startupdater.py'],
             pathex=['.'],
             excludes=map('encodings.'.__add__, encs))

upd_pyz = PYZ(upd_an.pure - [el for el in upd_an.pure if 'update' in el[1]])
upd_exe = EXE(upd_pyz,
              upd_an.scripts,
              upd_an.binaries,
              upd_an.zipfiles,
              name=os.path.join('dist', 'startupdater.exe' if sys.platform == 'win32' else 'startupdater'),
              debug=False,
              strip=False,
              upx=True,
              console=1,
              icon='develer.ico',
              append_pkg=False)

