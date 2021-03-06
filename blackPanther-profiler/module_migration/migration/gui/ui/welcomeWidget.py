#!/usr/bin/env python
# coding=UTF-8
#
# Generated by pykdeuic4 from welcomeWidget.ui on Fri Jul  4 20:21:40 2014
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_welcomeWidget(object):
    def setupUi(self, welcomeWidget):
        welcomeWidget.setObjectName(_fromUtf8("welcomeWidget"))
        welcomeWidget.resize(632, 410)
        welcomeWidget.setStyleSheet(_fromUtf8("color: black"))
        self.gridLayout = QtGui.QGridLayout(welcomeWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 150, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(17, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.labelMigrationIntro = QtGui.QLabel(welcomeWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Gothic L"))
        font.setPointSize(12)
        self.labelMigrationIntro.setFont(font)
        self.labelMigrationIntro.setStyleSheet(_fromUtf8("color: rgb(38, 44, 59);"))
        self.labelMigrationIntro.setFrameShadow(QtGui.QFrame.Raised)
        self.labelMigrationIntro.setWordWrap(True)
        self.labelMigrationIntro.setObjectName(_fromUtf8("labelMigrationIntro"))
        self.gridLayout.addWidget(self.labelMigrationIntro, 4, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(17, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 4, 5, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 156, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 5, 2, 1, 1)
        self.label = QtGui.QLabel(welcomeWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Gothic L"))
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(38, 44, 59);"))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 2, 1, 3)
        self.pixMigrationLogo = QtGui.QLabel(welcomeWidget)
        self.pixMigrationLogo.setStyleSheet(_fromUtf8(""))
        self.pixMigrationLogo.setFrameShadow(QtGui.QFrame.Raised)
        self.pixMigrationLogo.setText(_fromUtf8(""))
        self.pixMigrationLogo.setPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pics/miglogo.png")))
        self.pixMigrationLogo.setWordWrap(True)
        self.pixMigrationLogo.setObjectName(_fromUtf8("pixMigrationLogo"))
        self.gridLayout.addWidget(self.pixMigrationLogo, 3, 4, 3, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 4, 1, 1, 1)
        self.label_2 = QtGui.QLabel(welcomeWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Gothic L"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(38, 44, 59);"))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 3)

        self.retranslateUi(welcomeWidget)
        QtCore.QMetaObject.connectSlotsByName(welcomeWidget)

    def retranslateUi(self, welcomeWidget):
        welcomeWidget.setWindowTitle(kdecore.i18n("Welcome"))
        self.labelMigrationIntro.setText(kdecore.i18n(" Please click Next to transfer your files. \n"
"\n"
"blackPanther OS is a GNU/Linux distribution, targeting at computer literate users\' basic desktop needs; helps you connect to internet, read e-mails, work with office documents and more!"))
        self.label.setText(kdecore.i18n("blackPanther OS - Windows Migration Tool  "))
        self.label_2.setText(kdecore.i18n("This application, called Migration Tool, helps you transfer files and settings from other operating systems to blackPanther OS"))

import raw_rc

def encode(text):
    return text.encode('utf-8')
    