# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'threadexample.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ThreadExample(object):
    def setupUi(self, ThreadExample):
        ThreadExample.setObjectName("ThreadExample")
        ThreadExample.resize(711, 393)
        self.centralwidget = QtWidgets.QWidget(ThreadExample)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(68, 7, 466, 47))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.le_start_folder = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.le_start_folder.setObjectName("le_start_folder")
        self.horizontalLayout.addWidget(self.le_start_folder)
        self.bt_start = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.bt_start.setObjectName("bt_start")
        self.horizontalLayout.addWidget(self.bt_start)
        self.bt_cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.bt_cancel.setObjectName("bt_cancel")
        self.horizontalLayout.addWidget(self.bt_cancel)
        self.te_output = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.te_output.setGeometry(QtCore.QRect(67, 71, 607, 222))
        self.te_output.setObjectName("te_output")
        ThreadExample.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ThreadExample)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 711, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        ThreadExample.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ThreadExample)
        self.statusbar.setObjectName("statusbar")
        ThreadExample.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(ThreadExample)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(ThreadExample)
        self.actionClose.triggered.connect(ThreadExample.close)
        self.bt_start.clicked.connect(ThreadExample.start_listing)
        self.bt_cancel.clicked.connect(ThreadExample.cancel_listing)
        QtCore.QMetaObject.connectSlotsByName(ThreadExample)

    def retranslateUi(self, ThreadExample):
        _translate = QtCore.QCoreApplication.translate
        ThreadExample.setWindowTitle(_translate("ThreadExample", "MainWindow"))
        self.label.setText(_translate("ThreadExample", "Starting Folder "))
        self.bt_start.setText(_translate("ThreadExample", "Start"))
        self.bt_cancel.setText(_translate("ThreadExample", "Cancel"))
        self.menuFile.setTitle(_translate("ThreadExample", "File"))
        self.actionClose.setText(_translate("ThreadExample", "Close"))


