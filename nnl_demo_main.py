#!/usr/bin/env python

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_nnldemo import Ui_NNLDemo


class NNLDemoMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_NNLDemo()
        self.ui.setupUi(self)

        # Connect up menu actions
        # self.ui.actionExit.triggered.connect(self.close)

        # Connect up buttons.
        # self.ui.BUTTON_NAME.clicked.connect(self._pushed)
        self.ui.bt_yes.clicked.connect(self.handle_yes)
        self.ui.bt_no.clicked.connect(self.handle_no)

    def handle_yes(self):
        self.ui.le_user_name.setText("YES!")

    def handle_no(self):
        self.ui.le_user_name.setText("NO!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = NNLDemoMain()
    main.show()
    sys.exit(app.exec_())
