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

from PyQt4.QtCore import Qt, QRect, QSize
from PyQt4.QtGui import QApplication, QWidget, QGridLayout, QIcon
from PyQt4.QtGui import QHBoxLayout, QSpacerItem, QSizePolicy, QLabel
from PyQt4.QtGui import QComboBox, QPushButton, QSplitter
from PyQt4.QtGui import QVBoxLayout, QPlainTextEdit


class Ui_dev_client(object):
    def setupUi(self, dev_client):
        dev_client.resize(935, 660)
        dev_client.setWindowTitle(QApplication.translate("dev_client", "DevClient"))

        self.centralwidget = QWidget(dev_client)
        dev_client.setCentralWidget(self.centralwidget)

        main_layout = QGridLayout(self.centralwidget)
        main_layout.setContentsMargins(5, 5, 5, 3)
        main_layout.setSpacing(3)
        main_layout.setColumnStretch(0, 1)
        main_layout.setRowStretch(1, 1)

        top_layout = QHBoxLayout()
        top_layout.setContentsMargins(0, 0, 0, 0)
        top_layout.setSpacing(5)

        top_label_conn = QLabel()
        top_label_conn.setText(QApplication.translate("dev_client", "Connection"))
        top_layout.addWidget(top_label_conn)

        self.list_conn = QComboBox()
        self.list_conn.setFixedSize(145, 26)
        self.list_conn.setFocusPolicy(Qt.NoFocus)
        top_layout.addWidget(self.list_conn)

        self.list_account = QComboBox()
        self.list_account.setFixedSize(145, 26)
        self.list_account.setFocusPolicy(Qt.NoFocus)
        top_layout.addWidget(self.list_account)

        top_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        top_label_account = QLabel()
        top_label_account.setText(QApplication.translate("dev_client", "Account"))
        top_layout.addWidget(top_label_account)

        self.button_connect = QPushButton()
        self.button_connect.setFixedSize(105, 26)
        self.button_connect.setFocusPolicy(Qt.NoFocus)
        self.button_connect.setIcon(QIcon(":/images/connect.png"))
        self.button_connect.setIconSize(QSize(16, 16))
        self.button_connect.setText(QApplication.translate("dev_client", "Connect"))
        top_layout.addWidget(self.button_connect)

        self.button_option = QPushButton()
        self.button_option.setFixedSize(105, 26)
        self.button_option.setFocusPolicy(Qt.NoFocus)
        self.button_option.setIcon(QIcon(":/images/option.png"))
        self.button_option.setIconSize(QSize(16, 16))
        self.button_option.setText(QApplication.translate("dev_client", "Option"))
        top_layout.addWidget(self.button_option)
        main_layout.addLayout(top_layout, 0, 0)

        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.addItem(QSpacerItem(40, 29, QSizePolicy.Minimum, QSizePolicy.Fixed))

        self.rightpanel = QWidget()
        self.rightpanel.setMinimumWidth(225)
        right_layout.addWidget(self.rightpanel)
        main_layout.addLayout(right_layout, 0, 1, 3, 1)

        self.output_splitter = QSplitter(self.centralwidget)
        self.output_splitter.setOrientation(Qt.Vertical)
        self.output_splitter.setHandleWidth(3)
        self.output_splitter.setChildrenCollapsible(False)

        self.text_output = QPlainTextEdit(self.output_splitter)
        self.text_output.setMinimumWidth(690)
        self.text_output.setFocusPolicy(Qt.NoFocus)
        self.text_output.setAutoFillBackground(True)
        self.text_output.setUndoRedoEnabled(False)
        self.text_output.setReadOnly(True)

        self.text_output_noscroll = QPlainTextEdit(self.output_splitter)
        self.text_output_noscroll.setMinimumWidth(690)
        self.text_output_noscroll.setFocusPolicy(Qt.NoFocus)
        self.text_output_noscroll.setAutoFillBackground(True)
        self.text_output_noscroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.text_output_noscroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.text_output_noscroll.setUndoRedoEnabled(False)
        self.text_output_noscroll.setReadOnly(True)
        main_layout.addWidget(self.output_splitter, 1, 0)

        bottom_layout = QHBoxLayout()
        bottom_layout.setContentsMargins(0, 0, 0, 0)
        bottom_layout.setSpacing(5)

        self.text_input = QComboBox()
        self.text_input.setMinimumWidth(660)
        self.text_input.setFixedHeight(25)
        self.text_input.setEditable(True)
        self.text_input.addItem("")
        bottom_layout.addWidget(self.text_input)

        self.toggle_splitter = QPushButton()
        self.toggle_splitter.setFixedSize(25, 25)
        self.toggle_splitter.setFocusPolicy(Qt.NoFocus)
        self.toggle_splitter.setIcon(QIcon(":/images/split-window.png"))
        bottom_layout.addWidget(self.toggle_splitter)
        main_layout.addLayout(bottom_layout, 2, 0)
