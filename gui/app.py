#!/usr/bin/env python3


from ui.py.ui_main import Ui_Main
from password import PasswordDialog
from settings import SettingsDialog
from loading import LoadingDialog
from cocktails import cocktails
from PyQt5 import QtWidgets, QtCore, QtSerialPort, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QSize
import sys
import json
import copy

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class MainWindow(QMainWindow, Ui_Main):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_Main.__init__(self)
        self.setupUi(self)
        self.get_saved_ingredients()
        self.update_drink_list()
        self.serial = QtSerialPort.QSerialPort('/dev/ttyACM0', readyRead=self.receive)
        self.serial.open(QtCore.QIODevice.OpenModeFlag.ReadWrite)
        if not self.serial.isOpen():
            print("Initializing without Serial.")
        self.loadingDialog = LoadingDialog(self)
        self.passwordDialog = PasswordDialog(self)
        self.settingsDialog = SettingsDialog(self)
        self.init_animations()
        self.setWindowTitle("Choisissez une boisson!")
        self.settings.clicked.connect(self.open_password)

    def receive(self):
        while self.serial.canReadLine():
            text = self.serial.readLine().data().decode('ascii').strip('\r\n')
            if text == "Gobelet OK":
                pump = self.get_pump()
                # self.gif_gobelet.stop()
                self.gif_conveyor.start()
                self.loadingDialog.step.setText(f"Moving carpet to position {pump}")
                self.serial.write(f"C{pump};".encode())
            elif text == "Carpet OK":
                pump = self.get_pump()
                self.gif_conveyor.stop()
                self.gif_glass.start()
                self.loadingDialog.step.setText(f"Pumping at position {pump}")
                self.serial.write(f"P{pump}-{list(self.ing_dict.values())[0]};".encode())
                self.ing_dict.pop(list(self.ing_dict.keys())[0])
            elif text == "Pump OK":
                self.gif_glass.stop()
                self.gif_conveyor.start()
                if len(self.ing_dict) != 0:
                    pump = self.get_pump()
                    self.loadingDialog.step.setText(f"Moving carpet to position {pump}")
                    self.serial.write(f"C{pump};".encode())
                else:
                    self.loadingDialog.step.setText("Moving carpet to the end")
                    self.serial.write("End;".encode())
            elif text == "End OK":
                self.gif_conveyor.stop()
                self.loadingDialog.finishedDialog.setModal(True)
                self.loadingDialog.finishedDialog.show()

    def get_pump(self):
        key = list(self.ing_dict.keys())[0]
        if key == self.settingsDialog.name1.text():
            pump = 1
        elif key == self.settingsDialog.name2.text():
            pump = 2
        elif key == self.settingsDialog.name3.text():
            pump = 3
        elif key == self.settingsDialog.name4.text():
            pump = 4
        elif key == self.settingsDialog.name5.text():
            pump = 5
        elif key == self.settingsDialog.name6.text():
            pump = 6
        return pump

    def update_drink_list(self):
        self.scrollContents = QtWidgets.QWidget()
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollContents)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(20)
        self.create_cocktails()
        for i, cocktail in enumerate(self.current_cocktails):
            button = CustomButton(self, cocktail)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            button.setSizePolicy(sizePolicy)
            button.setMinimumSize(QtCore.QSize(300, 200))
            self.gridLayout.addWidget(button, i // 3, i % 3)
        self.verticalLayout.addLayout(self.gridLayout)
        self.scrollArea.setWidget(self.scrollContents)

    def create_cocktails(self):
        self.current_cocktails = []
        for name, cocktail_info in cocktails.items():
            n = 0
            for ingredient in cocktail_info[0].keys():
                if ingredient in self.current_ingredients:
                    n += 1
            if n == len(cocktail_info[0]):
                self.current_cocktails.append(name)

    def get_saved_ingredients(self):
        try:
            with open('save.json', 'r') as file:
                self.current_ingredients = json.load(file)
        except FileNotFoundError:
            self.current_ingredients = ['', '', '', '', '', '']

    def set_saved_ingredients(self):
        self.current_ingredients = [self.settingsDialog.name1.text(), self.settingsDialog.name2.text(), self.settingsDialog.name3.text(), self.settingsDialog.name4.text(), self.settingsDialog.name5.text(), self.settingsDialog.name6.text()]
        with open('save.json', 'w') as file:
            json.dump(self.current_ingredients, file)

    def open_password(self):
        self.passwordDialog.setModal(True)
        self.passwordDialog.show()

    def open_settings(self):
        self.settingsDialog.setModal(True)
        self.settingsDialog.show()

    def create_ing_dict(self, text):
        """Creates the dictionary of ingredients needed for the needed cocktail."""
        self.ing_dict = {}
        for key, value in cocktails.items():
            if key == text:
                self.ing_dict = copy.copy(value[0])
                break

    def init_animations(self):
        self.gif_conveyor = QtGui.QMovie(":/Logo/conveyor.gif")
        self.gif_conveyor.setScaledSize(QSize(512, 100))
        self.loadingDialog.conveyor.setMovie(self.gif_conveyor)
        self.gif_conveyor.start()
        self.gif_conveyor.stop()
        self.gif_glass = QtGui.QMovie(":/Logo/glass.gif")
        self.gif_glass.setScaledSize(QSize(100, 125))
        self.loadingDialog.glass.setMovie(self.gif_glass)
        self.gif_glass.start()
        self.gif_glass.stop()


class CustomButton(QtWidgets.QPushButton):
    def __init__(self, parent, name):
        QtWidgets.QPushButton.__init__(self, parent)
        self.setText(str(name))
        self.parent = parent

    def mousePressEvent(self, event):
        self.parent.create_ing_dict(self.text())
        self.parent.loadingDialog.step.setText("Dropping a cup...")
        # self.gif_gobelet.start()
        self.parent.loadingDialog.setModal(True)
        self.parent.loadingDialog.show()
        if not self.parent.serial.isOpen():
            print("No Serial. Sending: Gobelet;")
            self.parent.loadingDialog.manual()
        else:
            self.parent.serial.write("Gobelet;".encode())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
