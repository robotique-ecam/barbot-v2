#!/usr/bin/env python3


"""This is your app docstring."""


import sys
import time
from PyQt5 import QtCore
from ui_main import Ui_MainWindow
from ui_password import Ui_Dialog
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog


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
        self.password_dialog = PasswordDialog(self)
        self.drink1.clicked.connect(lambda: self.tabWidget.setCurrentIndex(1))
        self.drink1.clicked.connect(self.loading)

    def loading(self):
        """Progress bar function."""
        self.completed = 0
        self.password_dialog.show()
        while self.completed < 100:
            self.completed += 0.00001
            self.progress.setValue(self.completed)
        time.sleep(2)
        self.tabWidget.setCurrentIndex(2)


class PasswordDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        Ui_Dialog.__init__(self)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
