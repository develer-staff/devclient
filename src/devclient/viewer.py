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

import re
import storage
import logging

from sip import delete
from PyQt4.QtGui import QWidget, QTextCursor

logger = logging.getLogger('viewer')

def _setRightPanel(widget, server):

    widget_name = server.right_widget

    # delete the old widget
    map(delete, widget.rightpanel.children())

    if widget_name:
        try:
            parent = __import__('gui_src.' + widget_name, globals(), locals())
            module = getattr(parent, widget_name)

            class RightWidget(QWidget, module.Ui_RightWidget):
                def __init__(self, parent):
                    QWidget.__init__(self, parent)
                    self.setupUi(self, server)

        except ImportError:
            logger.warning('_setRightPanel: Unknown widget %s' % widget_name)
            return False
        else:
            widget.rightwidget = RightWidget(widget.rightpanel)
            widget.rightwidget.setVisible(True)

            # resize the window to display properly the new widget
            cur = widget.rightpanel.minimumWidth()
            new = widget.rightwidget.minimumWidth()
            widget.setMinimumWidth(widget.minimumWidth() + new - cur)
            widget.rightpanel.setMinimumWidth(new)

    return True


def getViewer(widget, server, custom_prompt=False):

    viewer = TextViewer(widget)
    if _setRightPanel(widget, server):
        if hasattr(server, 'prompt_reg') or custom_prompt:
            viewer = StatusViewer(viewer)

        if hasattr(server, 'wild_chars'):
            viewer = MapViewer(viewer, server.map_width, server.map_height)

    if hasattr(server, 'gui_width'):
        widget.resize(server.gui_width, widget.height())

    viewer._resetWidgets()
    return viewer


class TextViewer(object):
    """
    Build the html visualization from model.
    """

    MAX_ROWS = 1000
    """The max number of rows displayed in the TextEdit field"""

    _ROW_BLOCK = 20
    """The max number of rows per block"""

    def __init__(self, widget):
        self.w = widget
        doc = self.w.text_output.document()
        doc.setMaximumBlockCount(self.MAX_ROWS / self._ROW_BLOCK)
        self.w.text_output_noscroll.document().setMaximumBlockCount(40)
        self._cur_rows = 0
        self._no_scroll_text = []
        self._no_scroll_maxlen = 30

    def toggleSplitter(self):
        if self.w.text_output_noscroll.isVisible():
            self._appendToNoScroll()

    def _resetWidgets(self):
        self._textEditColors(self.w.text_output_noscroll)
        self._textEditColors(self.w.text_output)
        self.w.text_output_noscroll.clear()
        self.w.text_output.clear()

    def copySelectedText(self):
        """
        Copy the selected text from the text_output widget to clipboard.
        """

        def copyAndClean(widget):
            widget.copy()
            cursor = widget.textCursor()
            cursor.clearSelection()
            widget.setTextCursor(cursor)

        no_scroll = self.w.text_output_noscroll
        if no_scroll.textCursor().hasSelection() and no_scroll.isVisible():
            copyAndClean(no_scroll)
        elif self.w.text_output.textCursor().hasSelection():
            copyAndClean(self.w.text_output)
        elif self.w.text_input.lineEdit().hasSelectedText():
            self.w.text_input.lineEdit().copy()

    def appendHtml(self, html):
        new_html = html.split('<br>')
        cursor = self.w.text_output.textCursor()
        cursor.beginEditBlock()
        cursor.movePosition(QTextCursor.End)

        new_block = True
        while(new_html):
            if not self._cur_rows and not new_block:
                cursor.insertBlock()

            num_rows = len(new_html[:self._ROW_BLOCK - self._cur_rows])
            cursor.insertHtml('<br>'.join(new_html[:num_rows]))
            new_html = new_html[num_rows:]
            self._cur_rows = (num_rows + self._cur_rows) % self._ROW_BLOCK
            new_block = False

        cursor.endEditBlock()

        # move the cursor of text_output at the end of the scrollarea if
        # text_output_noscroll is hidden.
        if not self.w.text_output_noscroll.isVisible():
            self.w.text_output.setTextCursor(cursor)

        self._no_scroll_text += list(html.split('<br>'))
        # the buffer cache has a max length of self._no_scroll_maxlen
        self._no_scroll_text = self._no_scroll_text[-self._no_scroll_maxlen:]

        # For performance reasons, the widget self.w.text_output_noscroll is 
        # updated only if it is visible. Otherwise, its data is stored in the
        # cache self._no_scroll_text and it is updated only when became visible.
        if self.w.text_output_noscroll.isVisible():
            self._appendToNoScroll()

    def _appendToNoScroll(self):
        cursor = self.w.text_output_noscroll.textCursor()
        cursor.beginEditBlock()
        cursor.movePosition(QTextCursor.End)
        for i, row in enumerate(self._no_scroll_text):
            if i:
                cursor.insertBlock()
            cursor.insertHtml(row)
        cursor.endEditBlock()
        self.w.text_output_noscroll.setTextCursor(cursor)
        self._no_scroll_text = []

    def _textEditColors(self, text_edit):

        style = unicode(text_edit.styleSheet())
        m = re.search('QTextEdit\s*{(.*)}', style)
        if m:
            oldstyle = m.group(1)
            tmp = [el.split(':') for el in oldstyle.split(';') if el]
            d = dict([(k.strip(), v.strip()) for k, v in tmp])
        else:
            oldstyle = None
            d = {}

        d['color'] = storage.option('fg_color')
        d['background-color'] = storage.option('bg_color')

        newstyle = ';'.join([k + ':' + v for k, v in d.iteritems()])
        if oldstyle:
            text_edit.setStyleSheet(style.replace(oldstyle, newstyle))
        else:
            text_edit.setStyleSheet('QTextEdit {%s}' % newstyle)

    def process(self, model):
        self.appendHtml(model.main_html)


class StatusViewer(TextViewer):
    """
    Build the status visualization from model.

    This class is a subclass of `TextViewer` that take an instance of it
    as argument on __init__ (see `decorator pattern`_)

.. _decorator pattern: http://en.wikipedia.org/wiki/Decorator_pattern
    """

    def __init__(self, v):
        super(StatusViewer, self).__init__(v.w)
        self.v = v
        v.w.rightwidget.box_status.setVisible(True)
        self._last_values = {'Hp': None, 'Mn': None, 'Mv': None}

    def toggleSplitter(self):
        self.v.toggleSplitter()

    def process(self, model):
        self.v.process(model)

        stats = {'Hp': self.w.rightwidget.bar_health,
                 'Mn': self.w.rightwidget.bar_mana,
                 'Mv': self.w.rightwidget.bar_movement}

        if model.prompt:
            for k, bar in stats.iteritems():
                cur_value, max_value = model.prompt[k]
                cur_value = max(int(cur_value), 0)
                cur_value = min(int(max_value), cur_value)
                v = int(100 * cur_value / int(max_value))
                if v != self._last_values[k]:
                    self._last_values[k] = v
                    bar.setValue(v)

    def _resetWidgets(self):
        self.v._resetWidgets()


class MapViewer(TextViewer):
    """
    Build the visualization of a map from model.

    This class is a subclass of `TextViewer` that take an instance of it
    as argument on __init__ (see `decorator pattern`_)

.. _decorator pattern: http://en.wikipedia.org/wiki/Decorator_pattern
    """

    def __init__(self, v, map_width, map_height):
        super(MapViewer, self).__init__(v.w)
        self.v = v
        v.w.rightwidget.text_map.setVisible(True)
        self.map_width = map_width
        self.map_height = map_height

    def toggleSplitter(self):
        self.v.toggleSplitter()

    def _centerMap(self, model, width, height):
        html_list = model.map_html.split('<br>')
        text_list = model.map_text.split('\n')

        if len(text_list) > height:
            logger.warning('Map height: %d fixed height: %d' % 
                           (len(text_list), height))

        if max(map(len, text_list)) > width:
            logger.warning('Map width: %d fixed width: %d' % 
                           (max(map(len, text_list)), width))

        text, html = [], []
        for i, p in enumerate(text_list):
            if p.strip():
                html.append(html_list[i])
                text.append(p)

        delta_y = (height - len(text)) / 2
        delta_x = (width - len(max(text_list, key=len))) / 2
        model.map_text = '\n' * delta_y + \
            '\n'.join([' ' * delta_x + r for r in text])
        model.map_html = '<br>' * delta_y + \
            '<br>'.join(['&nbsp;' * delta_x + r for r in html])

    def process(self, model):
        self.v.process(model)
        w_map = self.w.rightwidget.text_map

        if model.map_text:
            w = self.map_width
            h = self.map_height
            self._centerMap(model, w, h)
            w_map.document().setHtml(model.map_html)
        elif model.map_text is None:
            w_map.document().clear()

    def _resetWidgets(self):
        self.v._resetWidgets()
        self._textEditColors(self.w.rightwidget.text_map)

