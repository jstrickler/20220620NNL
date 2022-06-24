# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nnldemo.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NNLDemo(object):
    def setupUi(self, NNLDemo):
        NNLDemo.setObjectName("NNLDemo")
        NNLDemo.resize(582, 428)
        self.centralwidget = QtWidgets.QWidget(NNLDemo)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(80, 190, 301, 121))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bt_yes = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.bt_yes.setObjectName("bt_yes")
        self.horizontalLayout_2.addWidget(self.bt_yes)
        self.bt_no = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.bt_no.setObjectName("bt_no")
        self.horizontalLayout_2.addWidget(self.bt_no)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 519, 149))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.le_user_name = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.le_user_name.setObjectName("le_user_name")
        self.horizontalLayout.addWidget(self.le_user_name)
        NNLDemo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NNLDemo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 582, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuComponents = QtWidgets.QMenu(self.menubar)
        self.menuComponents.setObjectName("menuComponents")
        self.menuValues = QtWidgets.QMenu(self.menubar)
        self.menuValues.setObjectName("menuValues")
        NNLDemo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NNLDemo)
        self.statusbar.setObjectName("statusbar")
        NNLDemo.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(NNLDemo)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtWidgets.QAction(NNLDemo)
        self.actionClose.setObjectName("actionClose")
        self.actionNew_thing = QtWidgets.QAction(NNLDemo)
        self.actionNew_thing.setObjectName("actionNew_thing")
        self.actionCut = QtWidgets.QAction(NNLDemo)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(NNLDemo)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(NNLDemo)
        self.actionPaste.setObjectName("actionPaste")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuComponents.addAction(self.actionNew_thing)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuComponents.menuAction())
        self.menubar.addAction(self.menuValues.menuAction())

        self.retranslateUi(NNLDemo)
        self.actionClose.triggered.connect(NNLDemo.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(NNLDemo)

    def retranslateUi(self, NNLDemo):
        _translate = QtCore.QCoreApplication.translate
        NNLDemo.setWindowTitle(_translate("NNLDemo", "Demo for NNL"))
        self.bt_yes.setText(_translate("NNLDemo", "Yes"))
        self.bt_no.setText(_translate("NNLDemo", "No"))
        self.label.setText(_translate("NNLDemo", "Your name"))
        self.menuFile.setTitle(_translate("NNLDemo", "File"))
        self.menuEdit.setTitle(_translate("NNLDemo", "Edit"))
        self.menuComponents.setTitle(_translate("NNLDemo", "Components"))
        self.menuValues.setTitle(_translate("NNLDemo", "Values"))
        self.actionOpen.setText(_translate("NNLDemo", "Open..."))
        self.actionClose.setText(_translate("NNLDemo", "Quit"))
        self.actionNew_thing.setText(_translate("NNLDemo", "New thing"))
        self.actionCut.setText(_translate("NNLDemo", "Cut"))
        self.actionCopy.setText(_translate("NNLDemo", "Copy"))
        self.actionPaste.setText(_translate("NNLDemo", "Paste"))