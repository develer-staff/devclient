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
encs -= set(['__init__', 'aliases', 'utf_8', 'latin_1', 'cp850'])

a = Analysis([os.path.join(HOMEPATH,'support/_mountzlib.py'),
              os.path.join(HOMEPATH,'support/useUnicode.py'),
              '../src/devclient/startcore.py'],
             pathex=['.'],
             excludes=map('encodings.'.__add__, encs))

pyz = PYZ(a.pure - [el for el in a.pure if 'devclient' in el[1]])
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          name=os.path.join('dist', 'startcore.exe' if sys.platform == 'win32' else 'startcore'),
          debug=False,
          strip=False,
          upx=False,
          console=1)
