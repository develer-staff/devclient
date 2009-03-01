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
:copyright: 2009 Gianni Valdambrini, Develer_ S.r.l.
:author: Gianni Valdambrini
:contact: gvaldambrini@develer.com

.. _Develer: http://www.develer.com/

The text below describe the procedure to build a setup installer for `Windows`
from scratch.

First of all, you have to install `Microsoft Visual Studio 2003` (you should use
`MinGW`, but the resulting packages are bigger than with `VS`), after which you
need to download and build the last source version of `Qt` for `Windows`.

To build `Qt` (with the purpose of reducing the footprint size of the generated
code), the configure step was executed with the command line:
configure.exe -release -static -no-accessibility -no-qt3support -no-opengl
    -platform win32-msvc2003 -no-exceptions -no-accessibility -no-stl -no-libmng
    -no-libtiff -no-openssl -no-dbus -no-phonon -no-phonon-backend -no-webkit

and the build step became the follow:
nmake sub-src

Download the last version of `Sip` and install using:
python configure.py
nmake
nmake install

Then download and install the last version of `PyQt4` with:
python configure.py --consolidate --enable=QtCore --enable=QtGui --enable=QtNetwork
nmake
nmake install

Now, you should have obtained a file named '_qt.pyd' under
<your_python_dir>/Lib/site-packages/PyQt4

You are ready to download and use `PyInstaller` (no installation required) from
the last svn version from its repository.
Before that, you have to do two things:
- download the last version of `upx` package for `Windows`, and set its main
  binary in the path of your system
- download and install the Python Windows extension named `pywin32`

Now you have to configure your `PyInstaller`, typing:
python Configure.py

Afterward, you have to download and install the last version of `Inno Setup` and
set the following enviroment variable:
- PYINSTALLER_PATH used to mark where is located your `PyInstaller` installation
- INNOSETUP_PATH used to mark where is located your `Inno Setup` installation

Finally, you have to execute the python script build_setup.py to obtain your
installer under the directory Output.

Note that build_setup.py is a two step script:
first build the packages (if they are missing) using the script build_packages.py
then create the `Inno Setup` installer.
"""

__docformat__ = 'restructuredtext'
