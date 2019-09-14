#!/usr/bin/env python3


"""This is your app docstring."""


import sys
from PyQt5 import QtCore, QtTest
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
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.drink1.clicked.connect(lambda: self.tabWidget.setCurrentIndex(1))
        self.drink1.clicked.connect(self.loading)
        self.settings.clicked.connect(self.ask_password)

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

    def ask_password(self):
        """Ask user for password using dialog."""
        passdiag = PasswordDialog(self)
        passdiag.setModal(True)
        passdiag.show()


class PasswordDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        Ui_Dialog.__init__(self)
        self.setupUi(self)
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.good_password = "8192"
        self.b0.clicked.connect(lambda: self.writing_password(self.b0))
        self.b1.clicked.connect(lambda: self.writing_password(self.b1))
        self.b2.clicked.connect(lambda: self.writing_password(self.b2))
        self.b3.clicked.connect(lambda: self.writing_password(self.b3))
        self.b4.clicked.connect(lambda: self.writing_password(self.b4))
        self.b5.clicked.connect(lambda: self.writing_password(self.b5))
        self.b6.clicked.connect(lambda: self.writing_password(self.b6))
        self.b7.clicked.connect(lambda: self.writing_password(self.b7))
        self.b8.clicked.connect(lambda: self.writing_password(self.b8))
        self.b9.clicked.connect(lambda: self.writing_password(self.b9))
        self.check.clicked.connect(self.check_password)
        self.erase.clicked.connect(self.erasing)

    def writing_password(self, button):
        if len(self.lineEdit.text()) < 6:
            self.lineEdit.setText(self.lineEdit.text() + button.text())

    def check_password(self):
        if self.lineEdit.text() == self.good_password:
            self.lineEdit.setText("")
            self.hide()
            self.parent().tabWidget.setCurrentIndex(3)
        else:
            self.lineEdit.setText("Wrong!")
            QtTest.QTest.qWait(1000)
            self.lineEdit.setText("")

    def erasing(self):
        if len(self.lineEdit.text()) > 0:
            self.lineEdit.setText(self.lineEdit.text()[:-1])
        else:
            self.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
