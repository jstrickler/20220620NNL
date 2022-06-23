#!/usr/bin/env python

import sys
import os

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QThread, pyqtSignal
from ui_threadexample import Ui_ThreadExample

class FileFetchThread(QThread):
    signal_update = pyqtSignal("PyQt_PyObject")
    signal_finished = pyqtSignal("PyQt_PyObject")

    def __init__(self, main):
        super().__init__()
        self._start_dir = None
        self._main = main

    def run(self):
        for dir_name, dirs, files in os.walk(self._start_dir):
            for file_name in files:
                if self._main._cancel_listing:
                    self.quit()
                    break
                file_path = os.path.join(dir_name, file_name)
                self.signal_update.emit(file_name)
        self.signal_finished.emit("DONE")

class ThreadExampleMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self._cancel_listing = False

        # Set up the user interface from Designer.
        self.ui = Ui_ThreadExample()
        self.ui.setupUi(self)

        self.file_fetch_thread = FileFetchThread(self)
        self.file_fetch_thread.signal_update.connect(self.update_files)
        self.file_fetch_thread.signal_finished.connect(self.finished)

    def update_files(self, new_file):
        self.ui.te_output.appendPlainText(new_file)

    def finished(self, _):
        self.ui.bt_start.setEnabled(True)

    def start_listing(self):
        self._cancel_listing = False
        self.ui.bt_start.setEnabled(False)
        start_dir = self.ui.le_start_folder.text()
        self.file_fetch_thread._start_dir = start_dir
        self.file_fetch_thread.start()

    def cancel_listing(self):
        self._cancel_listing = True
        self.ui.bt_start.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ThreadExampleMain()
    main.show()
    sys.exit(app.exec_())


