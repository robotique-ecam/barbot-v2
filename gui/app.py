#!/usr/bin/env python3

from PyQt5 import QtCore, QtTest
from ui_main import Ui_MainWindow
from password import PasswordDialog
from drink import DrinkDialog
from PyQt5.QtWidgets import QMainWindow, QApplication
import cocktails
import messages
import sys
import random
import serial
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
file_handler = RotatingFileHandler('activity.log', 'a', 1000000, 1)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)

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
        try:
            self.serial = serial.Serial(port='/dev/ttyACM0')
        except serial.SerialException:
            print("Serial not found")
        self.password_dialog = PasswordDialog(self)
        self.drink_dialog = DrinkDialog(self)
        self.setupUi(self)
        self.tabWidget.setCurrentIndex(0)
        self.button_clicked = self.picture1
        self.name_clicked = self.name1
        self.available_ingredients = []
        self.available_cocktails = []
        self.cocktails = []
        self.ingredients = []
        self.night_mode = False
        self.create_ingredients()
        self.create_drink_list()
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
        self.menuButton.clicked.connect(lambda: self.tabWidget.setCurrentIndex(0))
        self.new_drink.clicked.connect(lambda: self.tabWidget.setCurrentIndex(0))

    def create_ingredients(self):
        if self.night_mode:
            self.cocktails = cocktails.softs + cocktails.alcohols
        else:
            self.cocktails = cocktails.softs
        ing = []
        for i in range(0, len(self.cocktails)):
            ing += [ingredient for ingredient in self.cocktails[i][1].keys()]
        for ingredient in ing:
            if ingredient not in self.ingredients:
                self.ingredients.append(ingredient)

    def create_drink_list(self):
        drink_list = [self.drink1, self.drink2, self.drink3, self.drink4, self.drink5, self.drink6, self.drink7, self.drink8, self.drink9]
        for drink in drink_list:
            drink.setStyleSheet("")
            drink.setText("")
        if len(self.available_cocktails) < 1:
            self.drink1.setStyleSheet("background: transparent;")
        if len(self.available_cocktails) < 2:
            self.drink2.setStyleSheet("background: transparent;")
        if len(self.available_cocktails) < 3:
            self.drink3.setStyleSheet("background: transparent;")
        if len(self.available_cocktails) < 4:
            self.drink4.setStyleSheet("background: transparent;")
        if len(self.available_cocktails) < 5:
            self.drink5.setStyleSheet("background: transparent;")
        if len(self.available_cocktails) < 6:
            self.drink6.setStyleSheet("background: transparent;")
        if len(self.available_cocktails) < 7:
            self.drink7.setStyleSheet("background: transparent;")
        if len(self.available_cocktails) < 8:
            self.drink8.setStyleSheet("background: transparent;")
        if len(self.available_cocktails) < 9:
            self.drink9.setStyleSheet("background: transparent;")
        drinks_enabled = [drink for drink in drink_list if drink.styleSheet() == ""]
        i = 0
        for drink in drinks_enabled:
            drink.setText(self.available_cocktails[i][0])
            # icon = QtGui.QIcon()
            # icon.addPixmap(QtGui.QPixmap(":/Logo/test.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            # drink.setIcon(icon)
            i += 1

    def send_ingredients(self, button):
        ing_dict = {}
        for drink in self.available_cocktails:
            if drink[0] == button.text():
                ing_dict = drink[1]
                break
        for key, value in ing_dict.items():
            pump = 0
            if key == self.name1.text():
                pump = 1
            elif key == self.name2.text():
                pump = 2
            elif key == self.name3.text():
                pump = 3
            elif key == self.name4.text():
                pump = 4
            elif key == self.name5.text():
                pump = 5
            elif key == self.name6.text():
                pump = 6
            msg = "P" + str(pump) + "-" + str(value) + ";"
            try:
                self.serial.write(msg.encode())
                receive = ""
                while receive != "OK":
                    receive = self.serial.read_until(b'\r\n').decode('ascii').strip('\r\n')
                    logger.warning(str(receive.encode()))
                logger.warning('Out of loop')
            except AttributeError:
                print("No serial. Sending: " + msg)
        try:
            self.serial.write("End;".encode())
        except AttributeError:
            print("No serial. Sending: End;")

    def loading(self, button):
        """Progress bar function."""
        if button.styleSheet() == "":
            self.tabWidget.setCurrentIndex(1)
            self.send_ingredients(button)
            self.__step = 0
            self.timer = QtCore.QBasicTimer()
            self.timer.start(100, self)
            random.shuffle(messages.messages)
            for i in range(0, 100):
                if not self.timer.isActive():
                    break
                for j in range(0, 5):
                    if not self.timer.isActive():
                        break
                    self.preparing.setText(messages.messages[i % len(messages.messages)] + " .")
                    QtTest.QTest.qWait(500)
                    self.preparing.setText(messages.messages[i % len(messages.messages)] + " ..")
                    QtTest.QTest.qWait(500)
                    self.preparing.setText(messages.messages[i % len(messages.messages)] + " ...")
                    QtTest.QTest.qWait(500)

    def open_password(self):
        self.password_dialog.setModal(True)
        self.password_dialog.show()

    def open_drink(self, button):
        self.drink_dialog.list.clear()
        self.drink_dialog.list.insertItems(1, [' '] + self.ingredients)
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
        self.drink_dialog.picture.setStyleSheet(self.button_clicked.styleSheet())
        self.drink_dialog.name.setText(self.name_clicked.text())
        self.drink_dialog.setModal(True)
        self.drink_dialog.show()

    def timerEvent(self, e):
        """Increases step everytime it is called by timer."""
        if self.__step >= 100:
            self.timer.stop()
            self.tabWidget.setCurrentIndex(2)
            return
        self.__step = self.__step + 1
        self.progress.setValue(self.__step)

    """def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(100, self)"""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
