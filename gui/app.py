#!/usr/bin/env python3


"""This is your app docstring."""


import sys
import time
from PyQt5 import QtCore
from ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication


if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class MainWindow(QMainWindow, Ui_MainWindow):

    """Main board edition window."""

    def __init__(self):
        """Init."""
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.drink1.clicked.connect(lambda: self.tabWidget.setCurrentIndex(1))
        self.drink1.clicked.connect(self.loading)

    def loading(self):
        """Progress bar function."""
        self.completed = 0
        while self.completed < 100:
            self.completed += 0.00001
            self.progress.setValue(self.completed)
        time.sleep(2)
        self.tabWidget.setCurrentIndex(2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
