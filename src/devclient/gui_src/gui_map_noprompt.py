# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_map_noprompt.ui'
#
# Created: Mon Mar  3 23:36:58 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_RightWidget(object):
    def setupUi(self, RightWidget):
        RightWidget.setObjectName("RightWidget")
        RightWidget.resize(QtCore.QSize(QtCore.QRect(0,0,230,615).size()).expandedTo(RightWidget.minimumSizeHint()))
        RightWidget.setMinimumSize(QtCore.QSize(230,615))

        self.text_map = QtGui.QTextEdit(RightWidget)
        self.text_map.setGeometry(QtCore.QRect(0,0,225,231))
        self.text_map.setFocusPolicy(QtCore.Qt.NoFocus)
        self.text_map.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text_map.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text_map.setReadOnly(True)
        self.text_map.setProperty("char_width",QtCore.QVariant(27))
        self.text_map.setProperty("char_height",QtCore.QVariant(11))
        self.text_map.setObjectName("text_map")

        self.retranslateUi(RightWidget)
        QtCore.QMetaObject.connectSlotsByName(RightWidget)

    def retranslateUi(self, RightWidget):
        RightWidget.setWindowTitle(QtGui.QApplication.translate("RightWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.text_map.setStyleSheet(QtGui.QApplication.translate("RightWidget", "QTextEdit { background-color: #000000; font: 10pt \"Courier\"; color: #FFFFFF;}", None, QtGui.QApplication.UnicodeUTF8))
        self.text_map.setHtml(QtGui.QApplication.translate("RightWidget", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Courier\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

