#!/usr/bin/env python3


"""This is your app docstring."""


import sys
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

    def timerEvent(self, e):
        """Increases step by everytime it is called by timer."""
        if self.__step >= 100:
            self.timer.stop()
            self.tabWidget.setCurrentIndex(2)
            return
        self.__step = self.__step + 1
        self.progress.setValue(self.__step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(100, self)

    def loading(self):
        """Progress bar function."""
        self.__step = 0
        self.timer = QtCore.QBasicTimer()
        self.timer.start(100, self)


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
