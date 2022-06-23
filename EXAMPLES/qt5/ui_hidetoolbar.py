# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hidetoolbar.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HideToolbar(object):
    def setupUi(self, HideToolbar):
        HideToolbar.setObjectName("HideToolbar")
        HideToolbar.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(HideToolbar)
        self.centralwidget.setObjectName("centralwidget")
        HideToolbar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HideToolbar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        HideToolbar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HideToolbar)
        self.statusbar.setObjectName("statusbar")
        HideToolbar.setStatusBar(self.statusbar)

        self.retranslateUi(HideToolbar)
        QtCore.QMetaObject.connectSlotsByName(HideToolbar)

    def retranslateUi(self, HideToolbar):
        _translate = QtCore.QCoreApplication.translate
        HideToolbar.setWindowTitle(_translate("HideToolbar", "Hide Toolbar"))

