#!/usr/bin/env python
# coding=UTF-8
#
# Generated by pykdeuic4 from networkWidget.ui on Sun Jul  6 17:56:34 2014
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_networkWidget(object):
    def setupUi(self, networkWidget):
        networkWidget.setObjectName(_fromUtf8("networkWidget"))
        networkWidget.resize(585, 489)
        self.gridLayout_2 = QtGui.QGridLayout(networkWidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.layout = QtGui.QGridLayout()
        self.layout.setObjectName(_fromUtf8("layout"))
        self.gridLayout_2.addLayout(self.layout, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 3, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 2, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(networkWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Gothic L"))
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        spacerItem4 = QtGui.QSpacerItem(20, 15, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.frame = QtGui.QFrame(networkWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 80))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.labelMouseDesc = QtGui.QLabel(self.frame)
        self.labelMouseDesc.setGeometry(QtCore.QRect(10, 10, 521, 76))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMouseDesc.sizePolicy().hasHeightForWidth())
        self.labelMouseDesc.setSizePolicy(sizePolicy)
        self.labelMouseDesc.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Gothic L"))
        font.setPointSize(11)
        self.labelMouseDesc.setFont(font)
        self.labelMouseDesc.setStyleSheet(_fromUtf8("color: rgb(234, 225, 228);"))
        self.labelMouseDesc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelMouseDesc.setWordWrap(True)
        self.labelMouseDesc.setObjectName(_fromUtf8("labelMouseDesc"))
        self.pushNetButton = QtGui.QPushButton(self.frame)
        self.pushNetButton.setGeometry(QtCore.QRect(450, 50, 84, 24))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushNetButton.sizePolicy().hasHeightForWidth())
        self.pushNetButton.setSizePolicy(sizePolicy)
        self.pushNetButton.setObjectName(_fromUtf8("pushNetButton"))
        self.verticalLayout.addWidget(self.frame)
        spacerItem5 = QtGui.QSpacerItem(20, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem5)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 1, 1, 1)

        self.retranslateUi(networkWidget)
        QtCore.QMetaObject.connectSlotsByName(networkWidget)

    def retranslateUi(self, networkWidget):
        networkWidget.setWindowTitle(kdecore.i18n("Network"))
        self.label.setStyleSheet(kdecore.i18n("color: rgb(234, 225, 228);"))
        self.label.setText(kdecore.i18n("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'URW Gothic L\'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Connect to the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Internet or any Network</span></p></body></html>"))
        self.labelMouseDesc.setText(kdecore.i18n("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'URW Gothic L\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Can you managing all wired or wireless interface in the computer.  Please select an option. If you don\'t know what is this, please choose the \'Next\' button to other page.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.pushNetButton.setStatusTip(kdecore.i18n("Configure now network connections ...."))
        self.pushNetButton.setText(kdecore.i18n("Configure"))


def encode(text):
    return text.encode('utf-8')
    