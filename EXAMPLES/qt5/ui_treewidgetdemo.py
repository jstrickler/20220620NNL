# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'treewidgetdemo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TreeWidgetDemo(object):
    def setupUi(self, TreeWidgetDemo):
        TreeWidgetDemo.setObjectName("TreeWidgetDemo")
        TreeWidgetDemo.resize(578, 583)
        self.centralwidget = QtWidgets.QWidget(TreeWidgetDemo)
        self.centralwidget.setObjectName("centralwidget")
        self.tw_presidents = QtWidgets.QTreeWidget(self.centralwidget)
        self.tw_presidents.setGeometry(QtCore.QRect(40, 110, 291, 381))
        self.tw_presidents.setObjectName("tw_presidents")
        self.tw_presidents.headerItem().setText(0, "1")
        self.tw_presidents.header().setVisible(False)
        TreeWidgetDemo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TreeWidgetDemo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 578, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        TreeWidgetDemo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TreeWidgetDemo)
        self.statusbar.setObjectName("statusbar")
        TreeWidgetDemo.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(TreeWidgetDemo)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(TreeWidgetDemo)
        self.actionQuit.triggered.connect(TreeWidgetDemo.close)
        QtCore.QMetaObject.connectSlotsByName(TreeWidgetDemo)

    def retranslateUi(self, TreeWidgetDemo):
        _translate = QtCore.QCoreApplication.translate
        TreeWidgetDemo.setWindowTitle(_translate("TreeWidgetDemo", "MainWindow"))
        self.menuFile.setTitle(_translate("TreeWidgetDemo", "File"))
        self.actionQuit.setText(_translate("TreeWidgetDemo", "Quit"))

