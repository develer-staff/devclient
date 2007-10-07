#!/usr/bin/python
#-*- coding: utf-8 -*-

import re

from model import Model

class Parser(object):
    """
    The Parser class build a Model of data received.
    """

    __normal_color = ['000000','aa0000', '00aa00', 'aaaa00', '0000aa',
                      'aa00aa', '00aaaa', 'aaaaaa']

    __bright_color = ['444444','ff4444', '44ff44', 'ffff44', '4444ff',
                      'ff44ff', '44ffff', 'ffffff']

    def __init__(self):
        self.model = Model()

    def parse(self, data):
        """
        Parse data and build the Model object.
        """

        data = data.replace('\r', '')
        data = data.replace('\n', '<br>')
        data = data.replace(' ', '&nbsp;')
        data = self._replaceAnsiColor(data)
        self.model.mainTextAppend(data)

    def __getColor(self, index, attribute):
        if attribute:
            return self.__bright_color[index]
        else:
            return self.__normal_color[index]

    def _getStyle(self, ansi_code):

        attr = 0
        fg = None
        bg = None

        list_code = [int(c) for c in ansi_code.split(';')]

        for code in list_code:
            if 30 <= code <= 37:
                fg = code - 30
            elif 40 <= code <= 47:
                bg = code - 40
            elif code == 1:
                attr = 1

        style = []

        if fg is not None:
            style.append('color:#' + self.__getColor(fg, attr))

        if bg is not None:
            style.append('background-color:#' + self.__getColor(bg, attr))

        return ';'.join(style)

    def _replaceAnsiColor(self, data):

        START_TOKEN = chr(27) + '['
        COLOR_TOKEN = 'm'
        ANSI_CODE_UNSUPPORTED = ['H', 'f', 'A', 'B', 'C', 'D', 'R', 's', 'u',
                                 'J', 'K', 'h', 'l', 'p']

        ANSI_CODE = [COLOR_TOKEN]
        ANSI_CODE.extend(ANSI_CODE_UNSUPPORTED)

        parts = data.split(START_TOKEN)

        if len(parts) == 1:
            return parts[0]

        res = parts[0]
        reg = re.compile('(.*?)([%s])' % ''.join(ANSI_CODE), re.I)

        for s in parts[1:]:
            m = reg.match(s)
            if m:
                ansi_code = m.group(1)
                if m.group(2) == COLOR_TOKEN:
                    style = self._getStyle(ansi_code)
                    res += '<span style="%s">%s</span>' % \
                        (style, s[len(ansi_code) + 1 : ])
                else:
                    res += s[len(ansi_code) + 1 : ]
            else:
                res += s

        return res

