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


from PyQt4.QtGui import QApplication, QHBoxLayout, QFrame, QSpacerItem
from PyQt4.QtGui import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton
from PyQt4.QtGui import QComboBox, QIcon, QGroupBox, QCheckBox, QVBoxLayout
from PyQt4.QtGui import QListWidgetItem, QStackedLayout, QRadioButton
from PyQt4.QtGui import QListWidget, QSizePolicy, QListView
from PyQt4.QtCore import Qt, QVariant
from PyQt4 import QtCore, QtGui

import gui_option_rc
import gui_rc


class Ui_option(object):

    def createLine(self):
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        return line

    def createSquareLabel(self):
        label = QLabel()
        label.setEnabled(False)
        label.setFixedSize(24, 24)
        label.setFrameShape(QFrame.StyledPanel)
        return label

    def addVerticalStretch(self, page_layout):
        vert_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Expanding)
        page_layout.addItem(vert_spacer, page_layout.rowCount(), 0, 1, page_layout.columnCount())

    def createConnSection(self, page_layout, label, combobox, num_column):
        conn_layout = QHBoxLayout()
        conn_layout.setSpacing(5)
        conn_layout.setContentsMargins(0, 0, 0, 0)
        conn_layout.addWidget(label)
        conn_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum))
        conn_layout.addWidget(combobox, 1)

        page_layout.addLayout(conn_layout, page_layout.rowCount(), 0, 1, num_column)
        page_layout.addWidget(self.createLine(), page_layout.rowCount(), 0, 1, num_column)

        vert_spacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Fixed)
        page_layout.addItem(vert_spacer, page_layout.rowCount(), 0, 1, num_column)

    def createConnPage(self):
        self.conn_page = QWidget()
        self.conn_page.setObjectName("conn_page")

        page_layout = QGridLayout(self.conn_page)
        page_layout.setSpacing(7)
        page_layout.setContentsMargins(10, 20, 0, 10)
        page_layout.setColumnMinimumWidth(0, 100)

        self.label_conn = QLabel()
        self.label_conn.setText(QApplication.translate("option", "Connection"))
        page_layout.addWidget(self.label_conn, 0, 0)

        self.list_conn = QComboBox()
        self.list_conn.addItem(QApplication.translate("option", "Create New"))
        page_layout.addWidget(self.list_conn, 0, 1, 1, 2)

        self.label_name_conn = QLabel()
        self.label_name_conn.setText(QApplication.translate("option", "Name"))
        page_layout.addWidget(self.label_name_conn, 1, 0)

        self.name_conn = QLineEdit()
        page_layout.addWidget(self.name_conn, 1, 1, 1, 2)

        self.label_host_conn = QLabel()
        self.label_host_conn.setText(QApplication.translate("option", "Host"))
        page_layout.addWidget(self.label_host_conn, 2, 0)

        self.host_conn = QLineEdit()
        page_layout.addWidget(self.host_conn, 2, 1, 1, 2)

        self.label_port_conn = QLabel()
        self.label_port_conn.setText(QApplication.translate("option", "Port"))
        page_layout.addWidget(self.label_port_conn, 3, 0)

        page_layout.addItem(QSpacerItem(80, 20), 3, 1) # horizontal spacer

        self.port_conn = QLineEdit()
        self.port_conn.setMaxLength(8)
        page_layout.addWidget(self.port_conn, 3, 2)

        vert_spacer = QSpacerItem(271,20,QSizePolicy.Minimum,QSizePolicy.Fixed)
        page_layout.addItem(vert_spacer, 4, 0, 1, 3)

        buttons_box = QHBoxLayout()
        buttons_box.setSpacing(5)
        buttons_box.setContentsMargins(0, 0, 0, 0)

        self.save_conn = QPushButton()
        self.save_conn.setFixedHeight(28)
        self.save_conn.setIcon(QIcon(":/images/button-save.png"))
        self.save_conn.setText(QApplication.translate("option", "Save"))
        buttons_box.addWidget(self.save_conn)

        self.delete_conn = QPushButton()
        self.delete_conn.setFixedHeight(28)
        self.delete_conn.setIcon(QIcon(":/images/button-cancel.png"))
        self.delete_conn.setText(QApplication.translate("option", "Delete"))
        buttons_box.addWidget(self.delete_conn)

        page_layout.addLayout(buttons_box, 5, 0, 1, 3, Qt.AlignRight)
        self.addVerticalStretch(page_layout)
        self.page_container.addWidget(self.conn_page)

    def createAccountPage(self):
        self.account_page = QWidget()
        self.account_page.setObjectName("account_page")

        page_layout = QGridLayout(self.account_page)
        page_layout.setSpacing(10)
        page_layout.setContentsMargins(10, 20, 0, 10)
        page_layout.setColumnMinimumWidth(0, 130)

        self.save_account = QCheckBox()
        self.save_account.setText(QApplication.translate("option", "Save accounts"))

        self.label_conn_account = QLabel()
        self.label_conn_account.setText(QApplication.translate("option", "Connection"))

        self.list_conn_account = QComboBox()
        self.createConnSection(page_layout, self.label_conn_account, self.list_conn_account, 2)

        self.label_account_account = QLabel()
        self.label_account_account.setText(QApplication.translate("option", "Account"))
        page_layout.addWidget(self.label_account_account, 4, 0)

        self.list_account = QComboBox()
        page_layout.addWidget(self.list_account, 4, 1)

        buttons_box = QHBoxLayout()
        buttons_box.setSpacing(5)

        self.change_prompt = QPushButton()
        self.change_prompt.setEnabled(False)
        self.change_prompt.setFixedHeight(28)
        self.change_prompt.setIcon(QIcon(":/images/prompt.png"))
        self.change_prompt.setText(QApplication.translate("option", "Change Prompt"))
        buttons_box.addWidget(self.change_prompt)

        self.delete_account = QPushButton()
        self.delete_account.setEnabled(False)
        self.delete_account.setFixedHeight(28)
        self.delete_account.setIcon(QIcon(":/images/button-cancel.png"))
        self.delete_account.setText(QApplication.translate("option", "Delete"))
        buttons_box.addWidget(self.delete_account)
        page_layout.addLayout(buttons_box, 5, 0, 1, 2, Qt.AlignRight)

        self.box_prompt = QGroupBox()
        self.box_prompt.setTitle(QApplication.translate("option", "Prompt"))
        self.box_prompt.setToolTip(QApplication.translate("option", "<table>\n"
        "<tr><td colspan=3><b>Prompt format:</b></td></tr>\n"
        "<tr><td>%h</td><td>-></td><td>Current hit points</td></tr>\n"
        "<tr><td>%H</td><td>-></td><td>Maximum hit points</td></tr>\n"
        "<tr><td>%m</td><td>-></td><td>Current mana</td></tr>\n"
        "<tr><td>%M</td><td>-></td><td>Maximum mana</td></tr>\n"
        "<tr><td>%v</td><td>-></td><td>Current moves</td></tr>\n"
        "<tr><td>%V</td><td>-></td><td>Maximum moves</td></tr>\n"
        "<tr><td>*<td>-></td><td>Represent any char, repeated</td></tr>\n"
        "<tr><td colspan=2>&nbsp;</td><td>zero or more times</td></tr>\n"
        "<tr><td colspan=3>&nbsp;</td></tr>\n"
        "</table>\n"
        "<table>\n"
        "<tr><td colspan=3><b>Example:</b></td></tr>\n"
        "<tr><td colspan=3>[  %h/%Hhp %m/%Mmn %v/%Vmv *] ></td></tr>\n"
        "<tr><td colspan=3>is a valid representation for:</td></tr>\n"
        "<tr><td colspan=3>[  111/111hp 100/100mn 500/500mv 1000tnl] ></td></tr>\n"
        "</table>"))

        prompt_layout = QGridLayout(self.box_prompt)
        prompt_layout.setSpacing(5)
        prompt_layout.setContentsMargins(5, 5, 5, 5)

        label_normal = QLabel()
        label_normal.setText(QApplication.translate("option", "Normal"))
        prompt_layout.addWidget(label_normal, 0, 0)

        self.normal_prompt = QLineEdit()
        prompt_layout.addWidget(self.normal_prompt, 0, 1)

        label_fight = QLabel()
        label_fight.setText(QApplication.translate("option", "Fight"))
        prompt_layout.addWidget(label_fight, 1, 0)

        self.fight_prompt = QLineEdit()
        prompt_layout.addWidget(self.fight_prompt, 1, 1)

        self.save_prompt = QPushButton()
        self.save_prompt.setFixedHeight(28)
        self.save_prompt.setIcon(QIcon(":/images/button-save.png"))
        self.save_prompt.setText(QApplication.translate("option", "Save"))
        prompt_layout.addWidget(self.save_prompt, 2, 0, 1, 2, Qt.AlignRight)
        page_layout.addWidget(self.box_prompt, 6, 0, 1, 2)

        self.addVerticalStretch(page_layout)
        self.page_container.addWidget(self.account_page)

    def createAliasPage(self):
        self.alias_page = QWidget()
        self.alias_page.setObjectName("alias_page")

        page_layout = QGridLayout(self.alias_page)
        page_layout.setSpacing(7)
        page_layout.setContentsMargins(10, 20, 0, 10)
        page_layout.setColumnMinimumWidth(0, 80)

        self.label_conn_alias = QLabel()
        self.label_conn_alias.setText(QApplication.translate("option", "Connection"))
        self.list_conn_alias = QComboBox()
        self.createConnSection(page_layout, self.label_conn_alias, self.list_conn_alias, 3)

        self.label_alias_alias = QLabel()
        self.label_alias_alias.setText(QApplication.translate("option", "Alias"))
        page_layout.addWidget(self.label_alias_alias, 3, 0)

        page_layout.addItem(QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum), 3, 1)

        self.list_alias = QComboBox()
        self.list_alias.setEnabled(False)
        page_layout.addWidget(self.list_alias, 3, 2)

        self.label_label_alias = QLabel()
        self.label_label_alias.setText(QApplication.translate("option", "Label"))
        page_layout.addWidget(self.label_label_alias, 4, 0)

        page_layout.addItem(QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum), 4, 1)

        self.label_alias = QLineEdit()
        self.label_alias.setEnabled(False)
        page_layout.addWidget(self.label_alias, 4, 2)

        self.label_body_alias = QLabel()
        self.label_body_alias.setText(QApplication.translate("option", "Body"))
        page_layout.addWidget(self.label_body_alias, 5, 0)

        self.body_alias = QLineEdit()
        self.body_alias.setEnabled(False)
        page_layout.addWidget(self.body_alias, 5, 1, 1, 2)

        vert_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)
        page_layout.addItem(vert_spacer, 6, 0, 1, 3)

        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(5)
        buttons_layout.setContentsMargins(0, 0, 0, 0)

        self.save_alias = QPushButton()
        self.save_alias.setFixedHeight(28)
        self.save_alias.setIcon(QIcon(":/images/button-save.png"))
        self.save_alias.setText(QApplication.translate("option", "Save"))
        buttons_layout.addWidget(self.save_alias)

        self.delete_alias = QPushButton()
        self.delete_alias.setFixedHeight(28)
        self.delete_alias.setIcon(QIcon(":/images/button-cancel.png"))
        self.delete_alias.setText(QApplication.translate("option", "Delete"))
        buttons_layout.addWidget(self.delete_alias)
        page_layout.addLayout(buttons_layout, 7, 0, 1, 3, Qt.AlignRight)

        self.addVerticalStretch(page_layout)
        self.page_container.addWidget(self.alias_page)

    def createMacroPage(self):
        self.macro_page = QWidget()
        self.macro_page.setObjectName("macro_page")

        page_layout = QGridLayout(self.macro_page)
        page_layout.setSpacing(7)
        page_layout.setContentsMargins(10, 20, 0, 10)
        page_layout.setColumnMinimumWidth(0, 80)

        self.label_conn_macro = QLabel()

        self.list_conn_macro = QComboBox()
        self.createConnSection(page_layout, self.label_conn_macro, self.list_conn_macro, 3)

        self.label_macro_macro = QLabel()
        page_layout.addWidget(self.label_macro_macro, 4, 0)

        horiz_spacer = QSpacerItem(20, 20, QSizePolicy.Fixed,QSizePolicy.Minimum)
        page_layout.addItem(horiz_spacer, 4, 1)

        self.list_macro = QComboBox()
        self.list_macro.setEnabled(False)
        page_layout.addWidget(self.list_macro,4, 2)

        self.label_keys_macro = QLabel()
        page_layout.addWidget(self.label_keys_macro, 5, 0)

        self.register_macro = QPushButton()
        self.register_macro.setEnabled(False)
        self.register_macro.setFixedHeight(28)
        page_layout.addWidget(self.register_macro, 5, 1)

        self.keys_macro = QLineEdit()
        self.keys_macro.setEnabled(False)
        self.keys_macro.setProperty("highlight_color",QVariant("#C8C8C8"))
        page_layout.addWidget(self.keys_macro, 5, 2)

        self.label_command_macro = QLabel()
        page_layout.addWidget(self.label_command_macro, 6, 0)

        self.command_macro = QLineEdit()
        self.command_macro.setEnabled(False)
        page_layout.addWidget(self.command_macro, 6, 1, 1, 2)

        vert_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)
        page_layout.addItem(vert_spacer, 7, 0, 1, 3)

        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(5)
        buttons_layout.setContentsMargins(0, 0, 0, 0)

        self.save_macro = QPushButton()
        self.save_macro.setFixedHeight(28)
        self.save_macro.setIcon(QIcon(":/images/button-save.png"))
        buttons_layout.addWidget(self.save_macro)

        self.delete_macro = QPushButton()
        self.delete_macro.setFixedHeight(28)
        self.delete_macro.setIcon(QIcon(":/images/button-cancel.png"))
        buttons_layout.addWidget(self.delete_macro)
        page_layout.addLayout(buttons_layout, 8, 0, 1, 3, Qt.AlignRight)
        self.addVerticalStretch(page_layout)
        self.page_container.addWidget(self.macro_page)

        self.label_conn_macro.setText(QApplication.translate("option", "Connection"))
        self.label_macro_macro.setText(QApplication.translate("option", "Macro"))
        self.label_keys_macro.setText(QApplication.translate("option", "Keys"))
        self.label_command_macro.setText(QApplication.translate("option", "Command"))
        self.register_macro.setText(QApplication.translate("option", "Register"))
        self.save_macro.setText(QApplication.translate("option", "Save"))
        self.delete_macro.setText(QApplication.translate("option", "Delete"))

    def createTriggerPage(self):
        self.trigger_page = QWidget()
        self.trigger_page.setObjectName("trigger_page")

        page_layout = QGridLayout(self.trigger_page)
        page_layout.setSpacing(7)
        page_layout.setContentsMargins(10, 20, 0, 10)
        page_layout.setColumnMinimumWidth(1, 140)

        self.label_conn_trigger = QLabel()

        self.list_conn_trigger = QComboBox()
        self.createConnSection(page_layout, self.label_conn_trigger, self.list_conn_trigger, 2)

        self.label_trigger = QLabel()
        page_layout.addWidget(self.label_trigger, 3, 0, 1, 1)

        self.list_trigger = QComboBox()
        page_layout.addWidget(self.list_trigger, 3, 1, 1, 1)

        self.label_pattern_trigger = QLabel()
        page_layout.addWidget(self.label_pattern_trigger, 4, 0, 1, 1)

        self.pattern_trigger = QLineEdit()
        page_layout.addWidget(self.pattern_trigger, 4, 1, 1, 1)

        self.case_trigger = QCheckBox()
        page_layout.addWidget(self.case_trigger, 5, 0, 1, 2, Qt.AlignLeft)

        self.radio_command_trigger = QRadioButton()
        self.radio_command_trigger.setChecked(True)
        page_layout.addWidget(self.radio_command_trigger, 6, 0)

        self.command_trigger = QLineEdit()
        page_layout.addWidget(self.command_trigger, 6, 1)

        self.radio_color_trigger = QRadioButton()
        page_layout.addWidget(self.radio_color_trigger, 7, 0)

        horiz_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        page_layout.addItem(horiz_spacer, 7, 1)

        colors_layout = QHBoxLayout()
        colors_layout.setSpacing(3)

        self.text_color_trigger_button = QPushButton()
        self.text_color_trigger_button.setFixedHeight(28)
        self.text_color_trigger_button.setEnabled(False)
        self.text_color_trigger_button.setIcon(QIcon(":/images/button-color.png"))
        colors_layout.addWidget(self.text_color_trigger_button)

        self.text_color_trigger = self.createSquareLabel()
        colors_layout.addWidget(self.text_color_trigger)

        colors_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        colors_layout.addItem(colors_spacer)

        self.bg_color_trigger_button = QPushButton()
        self.bg_color_trigger_button.setEnabled(False)
        self.bg_color_trigger_button.setFixedHeight(28)
        self.bg_color_trigger_button.setIcon(QIcon(":/images/button-color.png"))
        colors_layout.addWidget(self.bg_color_trigger_button)

        self.bg_color_trigger = self.createSquareLabel()
        colors_layout.addWidget(self.bg_color_trigger)
        page_layout.addLayout(colors_layout, 8, 0, 1, 2)

        horiz_spacer2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        page_layout.addItem(horiz_spacer2, 9, 0, 1, 2)

        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(5)

        self.save_trigger = QPushButton()
        self.save_trigger.setFixedHeight(28)
        self.save_trigger.setIcon(QIcon(":/images/button-save.png"))
        buttons_layout.addWidget(self.save_trigger)

        self.delete_trigger = QPushButton()
        self.delete_trigger.setFixedHeight(28)
        self.delete_trigger.setIcon(QIcon(":/images/button-cancel.png"))
        buttons_layout.addWidget(self.delete_trigger)
        page_layout.addLayout(buttons_layout, 10, 0, 1, 2, Qt.AlignRight)
        self.page_container.addWidget(self.trigger_page)

        self.label_conn_trigger.setText(QApplication.translate("option", "Connection"))
        self.label_trigger.setText(QApplication.translate("option", "Trigger"))
        self.label_pattern_trigger.setText(QApplication.translate("option", "Pattern"))
        self.case_trigger.setText(QApplication.translate("option", "Ignore case"))
        self.radio_command_trigger.setText(QApplication.translate("option", "Command"))
        self.radio_color_trigger.setText(QApplication.translate("option", "Change color to"))
        self.text_color_trigger_button.setText(QApplication.translate("option", "Text"))
        self.text_color_trigger.setProperty("label_color", QVariant(True))
        self.bg_color_trigger_button.setText(QApplication.translate("option", "Background"))
        self.bg_color_trigger.setProperty("label_color", QVariant(True))
        self.save_trigger.setText(QApplication.translate("option", "Save"))
        self.delete_trigger.setText(QApplication.translate("option", "Delete"))

    def createPrefPage(self):
        self.pref_page = QWidget()
        self.pref_page.setObjectName("pref_page")

        page_layout = QVBoxLayout(self.pref_page)
        page_layout.setSpacing(7)
        page_layout.setContentsMargins(10, 20, 0, 10)

        textBox = QGroupBox()
        textBox.setTitle(QApplication.translate("option", "Text inserted"))
        text_layout = QGridLayout(textBox)
        text_layout.setSpacing(7)
        text_layout.setContentsMargins(10, 10, 10, 10)

        self.echo_color_button = QPushButton()
        self.echo_color_button.setFixedHeight(28)
        self.echo_color_button.setIcon(QIcon(":/images/button-color.png"))
        self.echo_color_button.setText(QApplication.translate("option", "Echo Color"))
        text_layout.addWidget(self.echo_color_button, 0, 0)

        self.echo_color = self.createSquareLabel()
        self.echo_color.setProperty('label_color', QVariant(True))
        text_layout.addWidget(self.echo_color, 0, 3)

        horiz_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        text_layout.addItem(horiz_spacer, 0, 4)

        self.label_cmd_separator = QLabel()
        self.label_cmd_separator.setText(QApplication.translate("option", "Command separator"))
        text_layout.addWidget(self.label_cmd_separator, 1, 0, 1, 2)

        self.cmd_separator = QLineEdit()
        self.cmd_separator.setFixedSize(24, 24)

        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.cmd_separator.setFont(font)
        self.cmd_separator.setMaxLength(1)
        self.cmd_separator.setAlignment(Qt.AlignCenter)
        text_layout.addWidget(self.cmd_separator, 1, 3)

        horiz_spacer2 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        text_layout.addItem(horiz_spacer2, 1, 4)

        self.keep_text = QCheckBox()
        self.keep_text.setText(QApplication.translate("option", "Keep text entered"))
        text_layout.addWidget(self.keep_text, 2, 0, 1, 4, Qt.AlignLeft)
        page_layout.addWidget(textBox)

        generalBox = QGroupBox()
        generalBox.setTitle(QApplication.translate("option", "General"))
        general_layout = QVBoxLayout(generalBox)
        general_layout.setSpacing(7)
        general_layout.setContentsMargins(10, 10, 10, 10)

        self.save_log = QCheckBox()
        self.save_log.setText(QApplication.translate("option", "Save log"))
        general_layout.addWidget(self.save_log, 0, Qt.AlignLeft)

        horiz_spacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        general_layout.addItem(horiz_spacer)
        page_layout.addWidget(generalBox)

        horiz_spacer2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        page_layout.addItem(horiz_spacer2)

        self.save_preferences = QPushButton()
        self.save_preferences.setFixedHeight(28)
        self.save_preferences.setIcon(QIcon(":/images/button-save.png"))
        self.save_preferences.setText(QApplication.translate("option", "Save"))
        page_layout.addWidget(self.save_preferences, 0, Qt.AlignRight)
        self.page_container.addWidget(self.pref_page)

    def populatePages(self):
        self.createConnPage()
        self.createAccountPage()
        self.createAliasPage()
        self.createMacroPage()
        self.createTriggerPage()
        self.createPrefPage()

    def createListOption(self):
        def addItem(label, icon_name):
            item = QListWidgetItem(list_option)
            item.setText(label)
            item.setTextAlignment(Qt.AlignHCenter)
            item.setIcon(QIcon(icon_name))

        list_option = QListWidget()
        list_option.setAutoFillBackground(True)
        list_option.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        list_option.setTextElideMode(Qt.ElideNone)
        list_option.setMovement(QListView.Static)
        list_option.setFlow(QListView.TopToBottom)
        list_option.setProperty("isWrapping", QVariant(False))
        list_option.setSpacing(3)
        list_option.setViewMode(QListView.IconMode)
        list_option.setUniformItemSizes(True)

        items = []
        items.append((QApplication.translate("option", "Connections"), ":/images/connections.png"))
        items.append((QApplication.translate("option", "Accounts"), ":/images/accounts.png"))
        items.append((QApplication.translate("option", "Aliases"), ":/images/aliases.png"))
        items.append((QApplication.translate("option", "Macros"), ":/images/macros.png"))
        items.append((QApplication.translate("option", "Triggers"), ":/images/triggers.png"))
        items.append((QApplication.translate("option", "Preferences"), ":/images/preferences.png"))

        max_length_label = ""
        for label, icon_name in items:
            addItem(label, icon_name)
            if len(label) > len(max_length_label):
                max_length_label = label

        w = list_option.fontMetrics().boundingRect(max_length_label).width()
        list_option.setFixedWidth(w + 20)
        return list_option

    def setupUi(self, option):
        option.setFixedSize(415, 385)
        option.setWindowTitle(QApplication.translate("option", "Option"))
        option.setStyleSheet("QLabel[label_color=\"true\"] { border: 1px solid gray; border-radius: 3px; } QListWidget { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #E0E0E0, stop: 1 #FFFFFF); color: #00AAFF;selection-background-color: #C8C8C8;selection-color:#000000;font: bold 10px \"Verdana\";  }")
        main_layout = QGridLayout(option)
        main_layout.setSpacing(5)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setColumnStretch(1, 1)

        self.list_option = self.createListOption()
        main_layout.addWidget(self.list_option, 0, 0)

        self.page_container = QStackedLayout()
        self.page_container.setContentsMargins(0, 0, 0, 0)
        self.populatePages()
        main_layout.addLayout(self.page_container, 0, 1)
        main_layout.addWidget(self.createLine(), 1, 0, 1, 2)

        close_layout = QHBoxLayout()
        close_layout.setContentsMargins(0, 0, 5, 0)
        close_layout.setSpacing(5)

        close_option = QPushButton()
        close_option.setText(QApplication.translate("option", "Close"))
        option.connect(close_option, QtCore.SIGNAL("clicked()"), option.accept)
        close_layout.addWidget(close_option)
        main_layout.addLayout(close_layout, 2, 1, 1, 2, Qt.AlignRight)

        self.list_option.setCurrentRow(0)
        self.page_container.setCurrentIndex(0)

        option.setTabOrder(self.list_option, self.list_conn)
        option.setTabOrder(self.list_conn, self.name_conn)
        option.setTabOrder(self.name_conn, self.host_conn)
        option.setTabOrder(self.host_conn, self.port_conn)
        option.setTabOrder(self.port_conn, self.save_conn)
        option.setTabOrder(self.save_conn, self.delete_conn)
        option.setTabOrder(self.delete_conn, self.list_conn_account)
        option.setTabOrder(self.list_conn_account, self.list_account)
        option.setTabOrder(self.list_account, self.delete_account)
        option.setTabOrder(self.delete_account, self.list_conn_alias)
        option.setTabOrder(self.list_conn_alias, self.list_alias)
        option.setTabOrder(self.list_alias, self.label_alias)
        option.setTabOrder(self.label_alias, self.body_alias)
        option.setTabOrder(self.body_alias, self.save_alias)
        option.setTabOrder(self.save_alias, self.delete_alias)
        option.setTabOrder(self.delete_alias, self.list_conn_macro)
        option.setTabOrder(self.list_conn_macro, self.list_macro)
        option.setTabOrder(self.list_macro, self.register_macro)
        option.setTabOrder(self.register_macro, self.keys_macro)
        option.setTabOrder(self.keys_macro, self.command_macro)
        option.setTabOrder(self.command_macro, self.save_macro)
        option.setTabOrder(self.save_macro, self.delete_macro)
        option.setTabOrder(self.delete_macro, self.echo_color_button)
        option.setTabOrder(self.echo_color_button, self.save_log)
