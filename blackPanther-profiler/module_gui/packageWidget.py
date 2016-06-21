#!/usr/bin/env python
# coding=UTF-8
#
# Generated by pykdeuic4 from sr./module_gui/packageWidget.ui on Wed Jul  2 19:58:35 2014
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_packageWidget(object):
    def setupUi(self, packageWidget):
        packageWidget.setObjectName(_fromUtf8("packageWidget"))
        packageWidget.resize(577, 505)
        self.gridLayout = QtGui.QGridLayout(packageWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBoxUpdates = QtGui.QGroupBox(packageWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxUpdates.sizePolicy().hasHeightForWidth())
        self.groupBoxUpdates.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Gothic L"))
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.groupBoxUpdates.setFont(font)
        self.groupBoxUpdates.setStyleSheet(_fromUtf8("color: rgb(234, 225, 228);"))
        self.groupBoxUpdates.setFlat(True)
        self.groupBoxUpdates.setObjectName(_fromUtf8("groupBoxUpdates"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBoxUpdates)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.showTray = QtGui.QCheckBox(self.groupBoxUpdates)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Gothic L"))
        font.setPointSize(11)
        self.showTray.setFont(font)
        self.showTray.setStyleSheet(_fromUtf8(""))
        self.showTray.setObjectName(_fromUtf8("showTray"))
        self.verticalLayout.addWidget(self.showTray)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.checkUpdate = QtGui.QCheckBox(self.groupBoxUpdates)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Gothic L"))
        font.setPointSize(11)
        self.checkUpdate.setFont(font)
        self.checkUpdate.setStyleSheet(_fromUtf8(""))
        self.checkUpdate.setObjectName(_fromUtf8("checkUpdate"))
        self.horizontalLayout.addWidget(self.checkUpdate)
        self.updateInterval = QtGui.QSpinBox(self.groupBoxUpdates)
        self.updateInterval.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Gothic L"))
        font.setPointSize(10)
        self.updateInterval.setFont(font)
        self.updateInterval.setMinimum(2)
        self.updateInterval.setObjectName(_fromUtf8("updateInterval"))
        self.horizontalLayout.addWidget(self.updateInterval)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addWidget(self.groupBoxUpdates)
        self.gridLayout.addLayout(self.verticalLayout_3, 5, 1, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.groupBoxRepo = QtGui.QGroupBox(packageWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Gothic L"))
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.groupBoxRepo.setFont(font)
        self.groupBoxRepo.setStyleSheet(_fromUtf8("color: rgb(234, 225, 228);"))
        self.groupBoxRepo.setFlat(True)
        self.groupBoxRepo.setObjectName(_fromUtf8("groupBoxRepo"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBoxRepo)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_3 = QtGui.QLabel(self.groupBoxRepo)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Gothic L"))
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.checkBoxContrib = QtGui.QCheckBox(self.groupBoxRepo)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Gothic L"))
        font.setPointSize(11)
        self.checkBoxContrib.setFont(font)
        self.checkBoxContrib.setStyleSheet(_fromUtf8(""))
        self.checkBoxContrib.setObjectName(_fromUtf8("checkBoxContrib"))
        self.verticalLayout_2.addWidget(self.checkBoxContrib)
        self.verticalLayout_4.addWidget(self.groupBoxRepo)
        self.gridLayout.addLayout(self.verticalLayout_4, 7, 1, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.labelProfilerIntro = QtGui.QLabel(packageWidget)
        self.labelProfilerIntro.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Gothic L"))
        font.setPointSize(11)
        self.labelProfilerIntro.setFont(font)
        self.labelProfilerIntro.setStyleSheet(_fromUtf8(""))
        self.labelProfilerIntro.setFrameShadow(QtGui.QFrame.Raised)
        self.labelProfilerIntro.setWordWrap(True)
        self.labelProfilerIntro.setObjectName(_fromUtf8("labelProfilerIntro"))
        self.horizontalLayout_2.addWidget(self.labelProfilerIntro)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 9, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 50, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 2, 1, 1, 1)
        self.label = QtGui.QLabel(packageWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
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
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem5, 4, 1, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem6, 6, 1, 1, 1)

        self.retranslateUi(packageWidget)
        QtCore.QMetaObject.connectSlotsByName(packageWidget)

    def retranslateUi(self, packageWidget):
        packageWidget.setWindowTitle(kdecore.i18n("Packages"))
        packageWidget.setStyleSheet(kdecore.i18n("color: rgb(234, 225, 228);"))
        self.groupBoxUpdates.setTitle(kdecore.i18n("Updates"))
        self.showTray.setText(kdecore.i18n("Show updates in the system tray"))
        self.checkUpdate.setText(kdecore.i18n("Check updates automatically every"))
        self.updateInterval.setStyleSheet(kdecore.i18n("color: #642437;"))
        self.updateInterval.setSuffix(kdecore.i18n(" hours"))
        self.groupBoxRepo.setTitle(kdecore.i18n("Repositories"))
        self.label_3.setText(kdecore.i18n("Contrib repository includes extra and handy programs."))
        self.checkBoxContrib.setText(kdecore.i18n("Add contrib repository"))
        self.labelProfilerIntro.setText(kdecore.i18n("To install and remove programs to blackPanther OS, use Package-Manager. Package-Manager also can automatically install the latest updates available. You can set the period for checking new updates."))
        self.label.setText(kdecore.i18n("Install / Remove Programs"))


def encode(text):
    return text.encode('utf-8')
    