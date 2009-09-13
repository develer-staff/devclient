#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Copyright (C) 2009 Gianni Valdambrini, Develer S.r.l (http://www.develer.com)
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

from PyQt4.QtGui import QVBoxLayout, QGridLayout, QApplication, QLabel
from PyQt4.QtGui import QProgressBar, QTextEdit, QWidget
from PyQt4.QtCore import QSize, Qt, QVariant


class Ui_RightWidget(object):
    def setupUi(self, RightWidget, server):
        RightWidget.setMinimumHeight(500)

        main_layout = QVBoxLayout(RightWidget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(10)

        # We hide all the main elements, to allow the proper viewer to enable
        # (only) the elements that uses.

        if hasattr(server, 'wild_chars'):
            self.text_map = QTextEdit()
            self.text_map.setObjectName('text_map')
            self.text_map.setVisible(False)
            self.text_map.setFocusPolicy(Qt.NoFocus)
            self.text_map.setAutoFillBackground(True)
            self.text_map.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.text_map.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.text_map.setUndoRedoEnabled(False)
            self.text_map.setReadOnly(True)
            # for some unknown reason, the fontmetrics of the text map is wrong
            # if the font is set with a global stylesheet, so we set it on the
            # specific widget.
            self.text_map.setStyleSheet("QTextEdit { font: 13px \"Courier\";}")
            main_layout.addWidget(self.text_map)

            # We calculate the map area size using the size of the font used. We
            # assume that the font is a monospace ones.
            font_metrics = self.text_map.fontMetrics()
            self.text_map.setFixedWidth(font_metrics.width('#' * server.map_width))
            self.text_map.setFixedHeight(font_metrics.height() * server.map_height)

            # The rightwidget width is determined by the map area size
            RightWidget.setMinimumWidth(self.text_map.width())
        else:
            RightWidget.setMinimumWidth(220)

        self.box_status = QWidget()
        self.box_status.setVisible(False)
        main_layout.addWidget(self.box_status)

        status_layout = QGridLayout(self.box_status)
        status_layout.setContentsMargins(5, 5, 5, 0)
        status_layout.setHorizontalSpacing(0)
        status_layout.setVerticalSpacing(15)

        label_health = QLabel()
        label_health.setMinimumWidth(80)
        label_health.setText(QApplication.translate("RightWidget", "Health"))
        status_layout.addWidget(label_health, 0, 0)

        self.bar_health = QProgressBar()
        self.bar_health.setObjectName("bar_health")
        self.bar_health.setFixedHeight(22)
        self.bar_health.setProperty("value", QVariant(100))
        self.bar_health.setTextVisible(False)
        status_layout.addWidget(self.bar_health, 0, 1)

        label_mana = QLabel()
        label_mana.setMinimumWidth(80)
        label_mana.setText(QApplication.translate("RightWidget", "Mana"))
        status_layout.addWidget(label_mana, 1, 0)

        self.bar_mana = QProgressBar()
        self.bar_mana.setObjectName("bar_mana")
        self.bar_mana.setFixedHeight(22)
        self.bar_mana.setProperty("value", QVariant(100))
        self.bar_mana.setTextVisible(False)
        status_layout.addWidget(self.bar_mana, 1, 1)

        label_movement = QLabel()
        label_movement.setMinimumWidth(80)
        label_movement.setText(QApplication.translate("RightWidget", "Movement"))
        status_layout.addWidget(label_movement, 2, 0)

        self.bar_movement = QProgressBar()
        self.bar_movement.setObjectName("bar_movement")
        self.bar_movement.setFixedHeight(22)
        self.bar_movement.setProperty("value", QVariant(100))
        self.bar_movement.setTextVisible(False)
        status_layout.addWidget(self.bar_movement, 2, 1)

        main_layout.addStretch()




