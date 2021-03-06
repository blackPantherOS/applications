#!/usr/bin/env python
# coding=UTF-8
#
# Generated by pykdeuic4 from summaryWidget2.ui on Fri Jul 11 07:30:17 2014
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_summaryWidget(object):
    def setupUi(self, summaryWidget):
        summaryWidget.setObjectName(_fromUtf8("summaryWidget"))
        summaryWidget.resize(615, 514)
        self.gridLayout = QtGui.QGridLayout(summaryWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.textSummary = QtGui.QTextEdit(summaryWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textSummary.sizePolicy().hasHeightForWidth())
        self.textSummary.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Gothic L"))
        font.setPointSize(10)
        self.textSummary.setFont(font)
        self.textSummary.setStyleSheet(_fromUtf8("#textSummary{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 81), stop:0.00537634 rgba(0, 0, 0, 80), stop:1 rgba(250, 250, 230, 80));\n"
"\n"
"border: 1px solid rgb(236, 236, 236, 80);\n"
"padding: 20px}\n"
""))
        self.textSummary.setObjectName(_fromUtf8("textSummary"))
        self.gridLayout.addWidget(self.textSummary, 2, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 5, 1, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(summaryWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Gothic L"))
        font.setPointSize(25)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8(""))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        spacerItem3 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.labelMouseDesc = QtGui.QLabel(summaryWidget)
        self.labelMouseDesc.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Gothic L"))
        font.setPointSize(11)
        self.labelMouseDesc.setFont(font)
        self.labelMouseDesc.setStyleSheet(_fromUtf8(""))
        self.labelMouseDesc.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelMouseDesc.setWordWrap(True)
        self.labelMouseDesc.setObjectName(_fromUtf8("labelMouseDesc"))
        self.verticalLayout_2.addWidget(self.labelMouseDesc)
        spacerItem4 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem4)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 0, 1, 1)

        self.retranslateUi(summaryWidget)
        QtCore.QMetaObject.connectSlotsByName(summaryWidget)

    def retranslateUi(self, summaryWidget):
        summaryWidget.setWindowTitle(kdecore.i18n("Summary"))
        summaryWidget.setStyleSheet(kdecore.i18n("color: rgb(234, 225, 228);"))
        self.label.setText(kdecore.i18n("Save Your Settings"))
        self.labelMouseDesc.setText(kdecore.i18n("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'URW Gothic L\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You have successfully finished all steps. Here\'s a summary of the settings you want to apply. Click <span style=\" font-weight:600;\">Apply Settings</span> to save them now or go back to appeal. You are now ready to enjoy blackPanther OS!</p></body></html>"))


def encode(text):
    return text.encode('utf-8')
    