# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_option.ui'
#
# Created: Mon Jan 14 22:49:12 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_option(object):
    def setupUi(self, option):
        option.setObjectName("option")
        option.resize(QtCore.QSize(QtCore.QRect(0,0,310,310).size()).expandedTo(option.minimumSizeHint()))
        option.setModal(True)

        self.tab_widget = QtGui.QTabWidget(option)
        self.tab_widget.setGeometry(QtCore.QRect(0,0,316,310))

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_widget.sizePolicy().hasHeightForWidth())
        self.tab_widget.setSizePolicy(sizePolicy)
        self.tab_widget.setObjectName("tab_widget")

        self.tab_conn = QtGui.QWidget()
        self.tab_conn.setObjectName("tab_conn")

        self.layoutWidget = QtGui.QWidget(self.tab_conn)
        self.layoutWidget.setGeometry(QtCore.QRect(10,10,291,266))
        self.layoutWidget.setObjectName("layoutWidget")

        self.gridlayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridlayout.setObjectName("gridlayout")

        self.gridlayout1 = QtGui.QGridLayout()
        self.gridlayout1.setObjectName("gridlayout1")

        self.label_conn = QtGui.QLabel(self.layoutWidget)
        self.label_conn.setObjectName("label_conn")
        self.gridlayout1.addWidget(self.label_conn,0,0,1,2)

        self.list_conn = QtGui.QComboBox(self.layoutWidget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_conn.sizePolicy().hasHeightForWidth())
        self.list_conn.setSizePolicy(sizePolicy)
        self.list_conn.setObjectName("list_conn")
        self.gridlayout1.addWidget(self.list_conn,0,2,1,2)

        self.label_name_conn = QtGui.QLabel(self.layoutWidget)
        self.label_name_conn.setMinimumSize(QtCore.QSize(45,0))
        self.label_name_conn.setMaximumSize(QtCore.QSize(45,16777215))
        self.label_name_conn.setObjectName("label_name_conn")
        self.gridlayout1.addWidget(self.label_name_conn,1,0,1,1)

        spacerItem = QtGui.QSpacerItem(45,20,QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Minimum)
        self.gridlayout1.addItem(spacerItem,1,1,1,1)

        self.name_conn = QtGui.QLineEdit(self.layoutWidget)
        self.name_conn.setObjectName("name_conn")
        self.gridlayout1.addWidget(self.name_conn,1,2,1,2)

        self.label_host_conn = QtGui.QLabel(self.layoutWidget)
        self.label_host_conn.setMinimumSize(QtCore.QSize(45,0))
        self.label_host_conn.setMaximumSize(QtCore.QSize(45,16777215))
        self.label_host_conn.setObjectName("label_host_conn")
        self.gridlayout1.addWidget(self.label_host_conn,2,0,1,1)

        spacerItem1 = QtGui.QSpacerItem(45,20,QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Minimum)
        self.gridlayout1.addItem(spacerItem1,2,1,1,1)

        self.host_conn = QtGui.QLineEdit(self.layoutWidget)
        self.host_conn.setObjectName("host_conn")
        self.gridlayout1.addWidget(self.host_conn,2,2,1,2)

        self.label_port_conn = QtGui.QLabel(self.layoutWidget)
        self.label_port_conn.setMinimumSize(QtCore.QSize(45,0))
        self.label_port_conn.setMaximumSize(QtCore.QSize(45,16777215))
        self.label_port_conn.setObjectName("label_port_conn")
        self.gridlayout1.addWidget(self.label_port_conn,3,0,1,1)

        spacerItem2 = QtGui.QSpacerItem(135,20,QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Minimum)
        self.gridlayout1.addItem(spacerItem2,3,1,1,2)

        self.port_conn = QtGui.QLineEdit(self.layoutWidget)
        self.port_conn.setMaxLength(8)
        self.port_conn.setObjectName("port_conn")
        self.gridlayout1.addWidget(self.port_conn,3,3,1,1)

        self.default_conn = QtGui.QCheckBox(self.layoutWidget)
        self.default_conn.setObjectName("default_conn")
        self.gridlayout1.addWidget(self.default_conn,4,0,1,4)
        self.gridlayout.addLayout(self.gridlayout1,0,0,1,2)

        spacerItem3 = QtGui.QSpacerItem(271,30,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem3,1,0,1,2)

        spacerItem4 = QtGui.QSpacerItem(20,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem4,2,0,1,1)

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setObjectName("hboxlayout")

        self.connect_conn = QtGui.QPushButton(self.layoutWidget)
        self.connect_conn.setEnabled(False)
        self.connect_conn.setObjectName("connect_conn")
        self.hboxlayout.addWidget(self.connect_conn)

        self.save_conn = QtGui.QPushButton(self.layoutWidget)
        self.save_conn.setObjectName("save_conn")
        self.hboxlayout.addWidget(self.save_conn)

        self.delete_conn = QtGui.QPushButton(self.layoutWidget)
        self.delete_conn.setObjectName("delete_conn")
        self.hboxlayout.addWidget(self.delete_conn)
        self.gridlayout.addLayout(self.hboxlayout,2,1,1,1)
        self.tab_widget.addTab(self.tab_conn,"")

        self.tab_alias = QtGui.QWidget()
        self.tab_alias.setObjectName("tab_alias")

        self.layoutWidget1 = QtGui.QWidget(self.tab_alias)
        self.layoutWidget1.setGeometry(QtCore.QRect(10,10,291,266))
        self.layoutWidget1.setObjectName("layoutWidget1")

        self.gridlayout2 = QtGui.QGridLayout(self.layoutWidget1)
        self.gridlayout2.setObjectName("gridlayout2")

        self.gridlayout3 = QtGui.QGridLayout()
        self.gridlayout3.setObjectName("gridlayout3")

        self.label_conn_alias = QtGui.QLabel(self.layoutWidget1)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_conn_alias.sizePolicy().hasHeightForWidth())
        self.label_conn_alias.setSizePolicy(sizePolicy)
        self.label_conn_alias.setMinimumSize(QtCore.QSize(66,0))
        self.label_conn_alias.setObjectName("label_conn_alias")
        self.gridlayout3.addWidget(self.label_conn_alias,0,0,1,2)

        self.list_conn_alias = QtGui.QComboBox(self.layoutWidget1)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_conn_alias.sizePolicy().hasHeightForWidth())
        self.list_conn_alias.setSizePolicy(sizePolicy)
        self.list_conn_alias.setObjectName("list_conn_alias")
        self.gridlayout3.addWidget(self.list_conn_alias,0,2,1,2)

        self.label_alias_alias = QtGui.QLabel(self.layoutWidget1)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_alias_alias.sizePolicy().hasHeightForWidth())
        self.label_alias_alias.setSizePolicy(sizePolicy)
        self.label_alias_alias.setMinimumSize(QtCore.QSize(66,0))
        self.label_alias_alias.setObjectName("label_alias_alias")
        self.gridlayout3.addWidget(self.label_alias_alias,1,0,1,1)

        spacerItem5 = QtGui.QSpacerItem(80,20,QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Minimum)
        self.gridlayout3.addItem(spacerItem5,1,1,1,2)

        self.list_alias = QtGui.QComboBox(self.layoutWidget1)
        self.list_alias.setEnabled(False)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_alias.sizePolicy().hasHeightForWidth())
        self.list_alias.setSizePolicy(sizePolicy)
        self.list_alias.setObjectName("list_alias")
        self.gridlayout3.addWidget(self.list_alias,1,3,1,1)

        self.label_label_alias = QtGui.QLabel(self.layoutWidget1)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_label_alias.sizePolicy().hasHeightForWidth())
        self.label_label_alias.setSizePolicy(sizePolicy)
        self.label_label_alias.setMinimumSize(QtCore.QSize(66,0))
        self.label_label_alias.setObjectName("label_label_alias")
        self.gridlayout3.addWidget(self.label_label_alias,2,0,1,1)

        spacerItem6 = QtGui.QSpacerItem(80,20,QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Minimum)
        self.gridlayout3.addItem(spacerItem6,2,1,1,2)

        self.label_alias = QtGui.QLineEdit(self.layoutWidget1)
        self.label_alias.setEnabled(False)
        self.label_alias.setObjectName("label_alias")
        self.gridlayout3.addWidget(self.label_alias,2,3,1,1)

        self.label_body_alias = QtGui.QLabel(self.layoutWidget1)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_body_alias.sizePolicy().hasHeightForWidth())
        self.label_body_alias.setSizePolicy(sizePolicy)
        self.label_body_alias.setMinimumSize(QtCore.QSize(66,0))
        self.label_body_alias.setObjectName("label_body_alias")
        self.gridlayout3.addWidget(self.label_body_alias,3,0,1,1)

        self.body_alias = QtGui.QLineEdit(self.layoutWidget1)
        self.body_alias.setEnabled(False)
        self.body_alias.setObjectName("body_alias")
        self.gridlayout3.addWidget(self.body_alias,3,1,1,3)
        self.gridlayout2.addLayout(self.gridlayout3,0,0,1,2)

        spacerItem7 = QtGui.QSpacerItem(271,66,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout2.addItem(spacerItem7,1,0,1,2)

        spacerItem8 = QtGui.QSpacerItem(91,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout2.addItem(spacerItem8,2,0,1,1)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.save_alias = QtGui.QPushButton(self.layoutWidget1)
        self.save_alias.setObjectName("save_alias")
        self.hboxlayout1.addWidget(self.save_alias)

        self.delete_alias = QtGui.QPushButton(self.layoutWidget1)
        self.delete_alias.setObjectName("delete_alias")
        self.hboxlayout1.addWidget(self.delete_alias)
        self.gridlayout2.addLayout(self.hboxlayout1,2,1,1,1)
        self.tab_widget.addTab(self.tab_alias,"")

        self.tab_macro = QtGui.QWidget()
        self.tab_macro.setObjectName("tab_macro")

        self.layoutWidget_2 = QtGui.QWidget(self.tab_macro)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10,10,291,266))
        self.layoutWidget_2.setObjectName("layoutWidget_2")

        self.gridlayout4 = QtGui.QGridLayout(self.layoutWidget_2)
        self.gridlayout4.setObjectName("gridlayout4")

        self.gridlayout5 = QtGui.QGridLayout()
        self.gridlayout5.setObjectName("gridlayout5")

        self.label_conn_macro = QtGui.QLabel(self.layoutWidget_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_conn_macro.sizePolicy().hasHeightForWidth())
        self.label_conn_macro.setSizePolicy(sizePolicy)
        self.label_conn_macro.setMinimumSize(QtCore.QSize(66,0))
        self.label_conn_macro.setObjectName("label_conn_macro")
        self.gridlayout5.addWidget(self.label_conn_macro,0,0,1,2)

        self.list_conn_macro = QtGui.QComboBox(self.layoutWidget_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_conn_macro.sizePolicy().hasHeightForWidth())
        self.list_conn_macro.setSizePolicy(sizePolicy)
        self.list_conn_macro.setObjectName("list_conn_macro")
        self.gridlayout5.addWidget(self.list_conn_macro,0,2,1,2)

        self.label_macro_macro = QtGui.QLabel(self.layoutWidget_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_macro_macro.sizePolicy().hasHeightForWidth())
        self.label_macro_macro.setSizePolicy(sizePolicy)
        self.label_macro_macro.setMinimumSize(QtCore.QSize(66,0))
        self.label_macro_macro.setObjectName("label_macro_macro")
        self.gridlayout5.addWidget(self.label_macro_macro,1,0,1,1)

        spacerItem9 = QtGui.QSpacerItem(80,20,QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Minimum)
        self.gridlayout5.addItem(spacerItem9,1,1,1,2)

        self.list_macro = QtGui.QComboBox(self.layoutWidget_2)
        self.list_macro.setEnabled(False)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_macro.sizePolicy().hasHeightForWidth())
        self.list_macro.setSizePolicy(sizePolicy)
        self.list_macro.setObjectName("list_macro")
        self.gridlayout5.addWidget(self.list_macro,1,3,1,1)

        self.label_keys_macro = QtGui.QLabel(self.layoutWidget_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_keys_macro.sizePolicy().hasHeightForWidth())
        self.label_keys_macro.setSizePolicy(sizePolicy)
        self.label_keys_macro.setMinimumSize(QtCore.QSize(66,0))
        self.label_keys_macro.setObjectName("label_keys_macro")
        self.gridlayout5.addWidget(self.label_keys_macro,2,0,1,1)

        self.keys_macro = QtGui.QLineEdit(self.layoutWidget_2)
        self.keys_macro.setEnabled(False)
        self.keys_macro.setProperty("highlight_color",QtCore.QVariant(QtGui.QApplication.translate("option", "#e0e0e0", None, QtGui.QApplication.UnicodeUTF8)))
        self.keys_macro.setObjectName("keys_macro")
        self.gridlayout5.addWidget(self.keys_macro,2,3,1,1)

        self.label_command_macro = QtGui.QLabel(self.layoutWidget_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_command_macro.sizePolicy().hasHeightForWidth())
        self.label_command_macro.setSizePolicy(sizePolicy)
        self.label_command_macro.setMinimumSize(QtCore.QSize(66,0))
        self.label_command_macro.setObjectName("label_command_macro")
        self.gridlayout5.addWidget(self.label_command_macro,3,0,1,1)

        self.command_macro = QtGui.QLineEdit(self.layoutWidget_2)
        self.command_macro.setEnabled(False)
        self.command_macro.setObjectName("command_macro")
        self.gridlayout5.addWidget(self.command_macro,3,1,1,3)

        self.register_macro = QtGui.QPushButton(self.layoutWidget_2)
        self.register_macro.setEnabled(False)
        self.register_macro.setObjectName("register_macro")
        self.gridlayout5.addWidget(self.register_macro,2,1,1,2)
        self.gridlayout4.addLayout(self.gridlayout5,0,0,1,2)

        spacerItem10 = QtGui.QSpacerItem(271,66,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout4.addItem(spacerItem10,1,0,1,2)

        spacerItem11 = QtGui.QSpacerItem(91,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout4.addItem(spacerItem11,2,0,1,1)

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setMargin(0)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.save_macro = QtGui.QPushButton(self.layoutWidget_2)
        self.save_macro.setObjectName("save_macro")
        self.hboxlayout2.addWidget(self.save_macro)

        self.delete_macro = QtGui.QPushButton(self.layoutWidget_2)
        self.delete_macro.setObjectName("delete_macro")
        self.hboxlayout2.addWidget(self.delete_macro)
        self.gridlayout4.addLayout(self.hboxlayout2,2,1,1,1)
        self.tab_widget.addTab(self.tab_macro,"")

        self.retranslateUi(option)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(option)
        option.setTabOrder(self.list_conn,self.name_conn)
        option.setTabOrder(self.name_conn,self.host_conn)
        option.setTabOrder(self.host_conn,self.port_conn)
        option.setTabOrder(self.port_conn,self.default_conn)
        option.setTabOrder(self.default_conn,self.connect_conn)
        option.setTabOrder(self.connect_conn,self.save_conn)
        option.setTabOrder(self.save_conn,self.delete_conn)
        option.setTabOrder(self.delete_conn,self.tab_widget)
        option.setTabOrder(self.tab_widget,self.list_conn_alias)
        option.setTabOrder(self.list_conn_alias,self.list_alias)
        option.setTabOrder(self.list_alias,self.label_alias)
        option.setTabOrder(self.label_alias,self.body_alias)
        option.setTabOrder(self.body_alias,self.save_alias)
        option.setTabOrder(self.save_alias,self.delete_alias)
        option.setTabOrder(self.delete_alias,self.list_conn_macro)
        option.setTabOrder(self.list_conn_macro,self.list_macro)
        option.setTabOrder(self.list_macro,self.register_macro)
        option.setTabOrder(self.register_macro,self.command_macro)
        option.setTabOrder(self.command_macro,self.save_macro)
        option.setTabOrder(self.save_macro,self.delete_macro)
        option.setTabOrder(self.delete_macro,self.keys_macro)

    def retranslateUi(self, option):
        option.setWindowTitle(QtGui.QApplication.translate("option", "Option", None, QtGui.QApplication.UnicodeUTF8))
        self.label_conn.setText(QtGui.QApplication.translate("option", "Connection", None, QtGui.QApplication.UnicodeUTF8))
        self.list_conn.addItem(QtGui.QApplication.translate("option", "Create New", None, QtGui.QApplication.UnicodeUTF8))
        self.label_name_conn.setText(QtGui.QApplication.translate("option", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_host_conn.setText(QtGui.QApplication.translate("option", "Host", None, QtGui.QApplication.UnicodeUTF8))
        self.label_port_conn.setText(QtGui.QApplication.translate("option", "Port", None, QtGui.QApplication.UnicodeUTF8))
        self.default_conn.setText(QtGui.QApplication.translate("option", "Make default", None, QtGui.QApplication.UnicodeUTF8))
        self.connect_conn.setText(QtGui.QApplication.translate("option", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.save_conn.setText(QtGui.QApplication.translate("option", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.delete_conn.setText(QtGui.QApplication.translate("option", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_conn), QtGui.QApplication.translate("option", "Connections", None, QtGui.QApplication.UnicodeUTF8))
        self.label_conn_alias.setText(QtGui.QApplication.translate("option", "Connection", None, QtGui.QApplication.UnicodeUTF8))
        self.label_alias_alias.setText(QtGui.QApplication.translate("option", "Alias", None, QtGui.QApplication.UnicodeUTF8))
        self.label_label_alias.setText(QtGui.QApplication.translate("option", "Label", None, QtGui.QApplication.UnicodeUTF8))
        self.label_body_alias.setText(QtGui.QApplication.translate("option", "Body", None, QtGui.QApplication.UnicodeUTF8))
        self.save_alias.setText(QtGui.QApplication.translate("option", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.delete_alias.setText(QtGui.QApplication.translate("option", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_alias), QtGui.QApplication.translate("option", "Alias", None, QtGui.QApplication.UnicodeUTF8))
        self.label_conn_macro.setText(QtGui.QApplication.translate("option", "Connection", None, QtGui.QApplication.UnicodeUTF8))
        self.label_macro_macro.setText(QtGui.QApplication.translate("option", "Macro", None, QtGui.QApplication.UnicodeUTF8))
        self.label_keys_macro.setText(QtGui.QApplication.translate("option", "Keys", None, QtGui.QApplication.UnicodeUTF8))
        self.label_command_macro.setText(QtGui.QApplication.translate("option", "Command", None, QtGui.QApplication.UnicodeUTF8))
        self.register_macro.setText(QtGui.QApplication.translate("option", "Register", None, QtGui.QApplication.UnicodeUTF8))
        self.save_macro.setText(QtGui.QApplication.translate("option", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.delete_macro.setText(QtGui.QApplication.translate("option", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_macro), QtGui.QApplication.translate("option", "Macro", None, QtGui.QApplication.UnicodeUTF8))
