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

__version__ = "$Revision$"[11:-2]
__docformat__ = 'restructuredtext'

import os
import ctypes
import signal
import smtplib
import subprocess
from sys import platform
from time import strftime
from traceback import format_exc
from sys import exc_info
from email.mime.text import MIMEText


# the smtp server used to send email
SMTP_SERVER = "smtp.develer.com"

EMAIL_FROM = "devclient@develer.com"
EMAIL_TO = "aleister@develer.com"

# Keypad codes for Windows platforms
_keypad_win_codes = {'7': 71, '8': 72, '9': 73,
                     '4': 75, '5': 76, '6': 77,
                     '1': 79, '2': 80, '3': 81,
                     '0': 82, '.': 83
                     }

# Keypad codes for Linux platforms
_keypad_linux_codes = {'7': 79, '8': 80, '9': 81,
                        '4': 83, '5': 84, '6': 85,
                        '1': 87, '2': 88, '3': 89,
                        '0': 90, '.': 91
                    }

# no keypad codes for Mac OSX (due to a limitation of the underlying platform)
keypad_codes = {}
if platform == 'win32':
    keypad_codes = _keypad_win_codes
elif platform == 'linux2':
    keypad_codes = _keypad_linux_codes


def terminateProcess(pid):
    """
    Kill a process.

    :Parameters:
      pid : int
        the id of the process to kill
    """

    if platform == 'win32':
        handle = ctypes.windll.kernel32.OpenProcess(1, False, pid)
        ctypes.windll.kernel32.TerminateProcess(handle, -1)
        ctypes.windll.kernel32.CloseHandle(handle)
    else:
        os.kill(pid, signal.SIGKILL)


def startProcess(cmd):
    """
    Launch a subprocess, hiding the console on win32.

    :Parameters:
      cmd : tuple
        the name and parameters of the process to launch.
    """

    if platform == 'win32':  # Hide console on win32 platform
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    else:
        startupinfo = None

    return subprocess.Popen(cmd, startupinfo=startupinfo)


def getExceptionInfo():
    """
    Return a detailed traceback of a fatal exception.
    """

    def extract_stack():
        tb = exc_info()[2]
        while tb.tb_next:
            tb = tb.tb_next

        stack = []
        f = tb.tb_frame
        while f:
            stack.append(f)
            f = f.f_back
        stack.reverse()

        return stack

    info = ["%s FATAL EXCEPTION %s %s" % 
                ('*' * 23, strftime("%Y-%m-%d %H:%M"), '*' * 23)]
    info.append(format_exc())
    info.append("%s" % ('+' * 80, ))
    stack = extract_stack()

    for frame in stack:
        info.append('')
        info.append("Frame %s in %s at line %s" % (frame.f_code.co_name,
                                                   frame.f_code.co_filename,
                                                   frame.f_lineno))
        for key, value in frame.f_locals.items():
            if key not in ('__doc__', '__docformat__', '__builtins__'):
                try:
                    info.append("%s = %s" % (key, value))
                except:
                    info.append("%s = <UNKNOWN VALUE>" % key)

    info.append("%s" % ('*' * 80, ))
    info.append('')
    return '\n'.join(info)


def sendMail(subject, body):
    """
    Send a textual email.

    :Parameters:
      subject : string
        the subject of the email.

      body : string
        the body of the email.
    """

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    server = smtplib.SMTP(SMTP_SERVER)
    server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    server.quit()


