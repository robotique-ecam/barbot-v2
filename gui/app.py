#!/usr/bin/env python3

from PyQt5 import QtCore, QtGui
from ui_main import Ui_MainWindow
from password import PasswordDialog
from drink import DrinkDialog
import cocktails
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
        self.available_ingredients = []
        self.available_cocktails = []
        self.cocktails = cocktails.cocktails
        self.create_drink_list()
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.settings.clicked.connect(self.open_password)
        self.drink1.clicked.connect(lambda: self.loading(self.drink1))
        self.drink2.clicked.connect(lambda: self.loading(self.drink2))
        self.drink3.clicked.connect(lambda: self.loading(self.drink3))
        self.drink4.clicked.connect(lambda: self.loading(self.drink4))
        self.drink5.clicked.connect(lambda: self.loading(self.drink5))
        self.drink6.clicked.connect(lambda: self.loading(self.drink6))
        self.drink7.clicked.connect(lambda: self.loading(self.drink7))
        self.drink8.clicked.connect(lambda: self.loading(self.drink8))
        self.drink9.clicked.connect(lambda: self.loading(self.drink9))
        self.picture1.clicked.connect(lambda: self.open_drink(self.picture1))
        self.picture2.clicked.connect(lambda: self.open_drink(self.picture2))
        self.picture3.clicked.connect(lambda: self.open_drink(self.picture3))
        self.picture4.clicked.connect(lambda: self.open_drink(self.picture4))
        self.picture5.clicked.connect(lambda: self.open_drink(self.picture5))
        self.picture6.clicked.connect(lambda: self.open_drink(self.picture6))

    def create_drink_list(self):
        drink_list = [self.drink1, self.drink2, self.drink3, self.drink4, self.drink5, self.drink6, self.drink7, self.drink8, self.drink9]
        for drink in drink_list:
            drink.show()
            sp = drink.sizePolicy()
            sp.setRetainSizeWhenHidden(True)
            drink.setSizePolicy(sp)
        if len(self.available_cocktails) < 1:
            self.drink1.hide()
        if len(self.available_cocktails) < 2:
            self.drink2.hide()
        if len(self.available_cocktails) < 3:
            self.drink3.hide()
        if len(self.available_cocktails) < 4:
            self.drink4.hide()
        if len(self.available_cocktails) < 5:
            self.drink5.hide()
        if len(self.available_cocktails) < 6:
            self.drink6.hide()
        if len(self.available_cocktails) < 7:
            self.drink7.hide()
        if len(self.available_cocktails) < 8:
            self.drink8.hide()
        if len(self.available_cocktails) < 9:
            self.drink9.hide()
        drinks_enabled = [drink for drink in drink_list if drink.isHidden() is False]
        i = 0
        for drink in drinks_enabled:
            drink.setText(self.available_cocktails[i][0])
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/Logo/test.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            drink.setIcon(icon)
            i += 1

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

    def loading(self, button):
        """Progress bar function."""
        self.tabWidget.setCurrentIndex(1)
        self.__step = 0
        self.timer = QtCore.QBasicTimer()
        self.timer.start(100, self)
        self.preparing.setText("Preparing " + button.text() + " ...")

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
