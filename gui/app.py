#!/usr/bin/env python3

from PyQt5 import QtCore
from ui_main import Ui_MainWindow
from password import PasswordDialog
from drink import DrinkDialog
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

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
        self.password_dialog = PasswordDialog(self)
        self.drink_dialog = DrinkDialog(self)
        self.setupUi(self)
        self.button_clicked = self.picture1
        self.name_clicked = self.name1
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.drink1.clicked.connect(self.loading)
        self.settings.clicked.connect(self.open_password)
        self.picture1.clicked.connect(lambda: self.open_drink(self.picture1))
        self.picture2.clicked.connect(lambda: self.open_drink(self.picture2))
        self.picture3.clicked.connect(lambda: self.open_drink(self.picture3))
        self.picture4.clicked.connect(lambda: self.open_drink(self.picture4))
        self.picture5.clicked.connect(lambda: self.open_drink(self.picture5))
        self.picture6.clicked.connect(lambda: self.open_drink(self.picture6))


    def timerEvent(self, e):
        """Increases step everytime it is called by timer."""
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
        self.tabWidget.setCurrentIndex(1)
        self.__step = 0
        self.timer = QtCore.QBasicTimer()
        self.timer.start(100, self)

    def open_password(self):
        self.password_dialog.setModal(True)
        self.password_dialog.show()

    def open_drink(self, button):
        self.button_clicked = button
        if button == self.picture1:
            self.name_clicked = self.name1
        if button == self.picture2:
            self.name_clicked = self.name2
        if button == self.picture3:
            self.name_clicked = self.name3
        if button == self.picture4:
            self.name_clicked = self.name4
        if button == self.picture5:
            self.name_clicked = self.name5
        if button == self.picture6:
            self.name_clicked = self.name6
        self.drink_dialog.setModal(True)
        self.drink_dialog.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
