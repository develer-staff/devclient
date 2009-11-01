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

import os
import os.path
from sys import path, argv, exit
from os.path import dirname, join, abspath, normpath

from constants import PROJECT_NAME
from utils import getExceptionInfo
from conf import loadConfiguration, config

from PyQt4.QtGui import QApplication, QStyleFactory

cfg_file = normpath(dirname(abspath(__file__)) + "/../../etc/devclient.cfg")


def main(argv=argv, cfg_file=cfg_file, update=1):
    """
    The function is the client entry point.
    """

    start_dir = os.getcwd()
    os.chdir(join(start_dir, dirname(argv[0]), dirname(cfg_file)))
    cfg_file = join(os.getcwd(), os.path.basename(cfg_file))
    loadConfiguration(cfg_file)
    os.chdir(start_dir)
    path.append(config['servers']['path'])
    path.append(config['configobj']['path'])

    # this import must stay here, after the appending of configobj path to path
    import storage
    storage.init(config['storage']['path'])

    # this import must stay here, after the appending of configobj path to path
    from gui import Gui
    try:
        app = QApplication([])
        app.setStyle(QStyleFactory.create("Cleanlooks"))

        gui = Gui(cfg_file)
        if not update:
            gui.displayWarning(PROJECT_NAME, gui._text['UpdateFail'])
        gui.show()
        exit(app.exec_())

    except Exception, e:
        print 'Fatal Exception:', e
        fd = open('exception.txt', 'a+')
        fd.write(getExceptionInfo())
        fd.close()


