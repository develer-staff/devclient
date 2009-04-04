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
This module is the client startup.
"""

__version__ = "$Revision$"[11:-2]
__docformat__ = 'restructuredtext'

import sys
from os import chdir
from subprocess import call
from os.path import dirname, join, abspath


if __name__ == '__main__':
    curr_dir = abspath(dirname(sys.argv[0]))
    script_dir = join(curr_dir, 'update')
    if hasattr(sys, 'frozen') and sys.frozen:
        retcode = call([join(script_dir, 'startupdater' +
                             ('.exe' if sys.platform == 'win32' else ''))])
    else:
        retcode = call(['python', join(script_dir, 'startupdater.py')])

    sys.path.append(join(curr_dir, 'src/devclient'))
    # This import must stay after the updating of the client
    import engine
    engine.main(update=not retcode)


