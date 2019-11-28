#!/usr/bin/env python3

from PyQt5 import QtCore, QtGui, QtSerialPort  # , QtTest
from ui_main import Ui_MainWindow
from password import PasswordDialog
from drink import DrinkDialog
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QSize, QIODevice
import cocktails
import messages
import sys
import random


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
        self.serial = QtSerialPort.QSerialPort('/dev/ttyACM0', readyRead=self.receive)
        self.serial.open(QIODevice.OpenModeFlag.ReadWrite)
        self.password_dialog = PasswordDialog(self)
        self.drink_dialog = DrinkDialog(self)
        self.setupUi(self)
        self.tabWidget.setCurrentIndex(0)
        self.button_clicked = self.picture1
        self.name_clicked = self.name1
        self.prev_step = 0
        self.available_ingredients = []
        self.available_cocktails = []
        self.cocktails = []
        self.ingredients = []
        self.night_mode = False
        self.create_ingredients()
        self.create_drink_list()
        self.gif_conveyor = QtGui.QMovie(":/Logo/conveyor.gif")
        self.gif_conveyor.setScaledSize(QSize(512, 100))
        self.conveyor.setMovie(self.gif_conveyor)
        self.gif_conveyor.start()
        self.gif_conveyor.stop()
        self.gif_glass = QtGui.QMovie(":/Logo/glass.gif")
        self.gif_glass.setScaledSize(QSize(100, 125))
        self.glass.setMovie(self.gif_glass)
        self.gif_glass.start()
        self.gif_glass.stop()
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
        self.carpet_left.pressed.connect(self.carpet_left_start)
        self.carpet_left.released.connect(self.carpet_stop)
        self.carpet_right.pressed.connect(self.carpet_right_start)
        self.carpet_right.released.connect(self.carpet_stop)

    def receive(self):
        while self.serial.canReadLine():
            text = self.serial.readLine().data().decode('ascii').strip('\r\n')
            print(text)
            if text == "Gobelet OK":
                pump = self.getPump(self.ing_dict)
                # self.gif_gobelet.stop()
                self.gif_conveyor.start()
                self.preparing.setText("Moving carpet to position " + str(pump))
                msgC = "C" + str(pump) + ";"
                self.serial.write(msgC.encode())
            elif text == "Carpet OK":
                pump = self.getPump(self.ing_dict)
                self.gif_conveyor.stop()
                self.gif_glass.start()
                self.preparing.setText("Pumping at position " + str(pump))
                msgP = "P" + str(pump) + "-" + str(list(self.ing_dict.values())[0]) + ";"
                self.serial.write(msgP.encode())
                self.ing_dict.pop(list(self.ing_dict.keys())[0])
            elif text == "Pump OK":
                self.gif_glass.stop()
                self.gif_conveyor.start()
                if len(self.ing_dict) != 0:
                    pump = self.getPump(self.ing_dict)
                    self.preparing.setText("Moving carpet to position " + str(pump))
                    msgC = "C" + str(pump) + ";"
                    self.serial.write(msgC.encode())
                else:
                    self.preparing.setText("Moving carpet to the end")
                    self.serial.write("End;".encode())
            elif text == "End OK":
                self.gif_conveyor.stop()
                self.tabWidget.setCurrentIndex(2)

    def getPump(self, dict):
        key = list(dict.keys())[0]
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
        return pump

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
            drink.raise_()
            drink.setText("")
        if len(self.available_cocktails) < 1:
            self.drink1.lower()
        if len(self.available_cocktails) < 2:
            self.drink2.lower()
        if len(self.available_cocktails) < 3:
            self.drink3.lower()
        if len(self.available_cocktails) < 4:
            self.drink4.lower()
        if len(self.available_cocktails) < 5:
            self.drink5.lower()
        if len(self.available_cocktails) < 6:
            self.drink6.lower()
        if len(self.available_cocktails) < 7:
            self.drink7.lower()
        if len(self.available_cocktails) < 8:
            self.drink8.lower()
        if len(self.available_cocktails) < 9:
            self.drink9.lower()
        drinks_enabled = [drink_list[i] for i in range(len(self.available_cocktails))]
        i = 0
        for drink in drinks_enabled:
            drink.setText(self.available_cocktails[i][0])
            # icon = QtGui.QIcon()
            # icon.addPixmap(QtGui.QPixmap(":/Logo/test.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            # drink.setIcon(icon)
            i += 1

    def create_ing_dict(self, button):
        self.ing_dict = {}
        for drink in self.available_cocktails:
            if drink[0] == button.text():
                self.ing_dict = drink[1]
                break
        # self.num_ingredients = 2*len(ing_dict) + 1

    def loading(self, button):
        self.create_ing_dict(button)
        self.tabWidget.setCurrentIndex(1)
        self.preparing.setText("Dropping a cup...")
        self.serial.write("Gobelet;".encode())
        # self.__step = 0
        # self.timer = QtCore.QBasicTimer()
        # self.timer.start(10, self)
        random.shuffle(messages.messages)
        """for i in range(0, 100):
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
                QtTest.QTest.qWait(500)"""

    def open_password(self):
        self.password_dialog.setModal(True)
        self.password_dialog.show()

    def open_drink(self, button):
        self.drink_dialog.list.clear()
        self.drink_dialog.list.insertItems(1, [' '] + self.ingredients)
        self.drink_dialog.list.setCurrentText(self.name_clicked.text())
        self.button_clicked = button
        if button == self.picture1:
            self.name_clicked = self.name1
        elif button == self.picture2:
            self.name_clicked = self.name2
        elif button == self.picture3:
            self.name_clicked = self.name3
        elif button == self.picture4:
            self.name_clicked = self.name4
        elif button == self.picture5:
            self.name_clicked = self.name5
        elif button == self.picture6:
            self.name_clicked = self.name6
        self.drink_dialog.picture.setStyleSheet(self.button_clicked.styleSheet())
        self.drink_dialog.name.setText(self.name_clicked.text())
        self.drink_dialog.setModal(True)
        self.drink_dialog.show()

    def timerEvent(self, e):
        """Increases step everytime it is called by timer."""
        if self.__step == 100:
            self.timer.stop()
            self.tabWidget.setCurrentIndex(2)
            return
        """elif self.prev_step >= self.__step % (100 / self.num_ingredients) and self.__step != 0:
            self.timer.stop()
            try:
                receive = ""
                while receive != "OK":
                    receive = self.serial.read_until(b'\r\n').decode('ascii').strip('\r\n')
            except AttributeError:
                print("No serial. Waiting 500ms ({0}%)".format(self.__step))
                QtTest.QTest.qWait(1000)
            self.timer.start(10, self)

        self.prev_step = self.__step % (100 / self.num_ingredients)"""
        self.__step += 1
        self.progress.setValue(self.__step)

    def carpet_left_start(self):
        msg = "RC;"
        try:
            self.serial.write(msg.encode())
        except AttributeError:
            print("No serial. Sending: " + msg)

    def carpet_right_start(self):
        msg = "FC;"
        try:
            self.serial.write(msg.encode())
        except AttributeError:
            print("No serial. Sending: " + msg)

    def carpet_stop(self):
        msg = "S;"
        try:
            self.serial.write(msg.encode())
        except AttributeError:
            print("No serial. Sending: " + msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
