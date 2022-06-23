#!/usr/bin/env python
import sys
import random

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtTest import QTest
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot

from ui_tabsthread import Ui_TabsThread

class ChatWorker(QObject):
    finished = pyqtSignal()

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

    @pyqtSlot()
    def update_chat(self): # slot takes no params
        with open('../../DATA/words.txt') as words_in:
            for i, line in enumerate(words_in, 1):
                QTest.qWait(random.randint(20, 200))
                self.main_window.ui.te_chat.appendPlainText(line.rstrip())
                if i == 100:
                    break
        self.finished.emit()

class DataWorker(QObject):
    finished = pyqtSignal()

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

    @pyqtSlot()
    def update_data(self):
        with open('../../DATA/words.txt') as words_in:
            for i, line in enumerate(words_in, 1):
                QTest.qWait(random.randint(10, 150))
                self.main_window.ui.te_data.appendPlainText(line.rstrip().upper())
                if i == 50:
                    break
        self.finished.emit()


class TabsThreadMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_TabsThread()
        self.ui.setupUi(self)
        self.ui.tabs.setCurrentIndex(0)

        self._setup_chat_thread()
        self._setup_data_thread()

    def _setup_data_thread(self):
        self.data_obj = DataWorker(self)
        self.data_thread = QThread()
        self.data_obj.moveToThread(self.data_thread)
        self.data_thread.started.connect(self.data_obj.update_data)
        self.data_thread.start()
        self.data_obj.finished.connect(self.data_thread.quit)
        self.data_thread.finished.connect(self.data_done)

    def _setup_chat_thread(self):
        self.chat_obj = ChatWorker(self)
        self.chat_thread = QThread()
        self.chat_obj.moveToThread(self.chat_thread)
        self.chat_thread.started.connect(self.chat_obj.update_chat)
        self.chat_thread.start()
        self.chat_obj.finished.connect(self.chat_thread.quit)
        self.chat_thread.finished.connect(self.chat_done)

    def chat_done(self):
        self.show_popup("Chat is done")

    def data_done(self):
        self.show_popup("Data is done")

    def show_popup(self, message):
        QMessageBox.information(self, "Progress", message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TabsThreadMain()
    main.show()
    sys.exit(app.exec_())


