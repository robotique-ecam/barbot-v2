#!/usr/bin/env python3

from ui_drink import Ui_Dialog
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtGui


class DrinkDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        Ui_Dialog.__init__(self)
        self.setupUi(self)
        self.ok.clicked.connect(self.update_drinks)
        self.pump.pressed.connect(self.pump_start)
        self.pump.released.connect(self.pump_stop)
        self.purge.pressed.connect(self.purge_start)
        self.purge.released.connect(self.pump_stop)

    def update_drinks(self):
        """Updating image and name of ingredient on the admin tab."""
        self.parent().name_clicked.setText(self.list.currentText())
        for drink in self.parent().cocktails:
            if drink[0] == self.parent().name_clicked.text():
                self.parent().name_clicked.setFont(QtGui.QFont("Verdana", drink[2] / 2))
        if self.parent().name_clicked.text() == " ":
            self.parent().button_clicked.setStyleSheet("")
        elif self.parent().name_clicked.text() == "Water":
            self.parent().button_clicked.setStyleSheet("background-image: url(:/Logo/test.png)")
        elif self.parent().name_clicked.text() == "Beer":
            self.parent().button_clicked.setStyleSheet("background-image: url(:/Logo/test.png)")
        self.parent().available_ingredients = [self.parent().name1.text(), self.parent().name2.text(), self.parent().name3.text(), self.parent().name4.text(), self.parent().name5.text(), self.parent().name6.text()]

        """Updating list of available cocktails from the available ingredients."""
        self.parent().available_cocktails = []
        for cocktail in self.parent().cocktails:
            n = 0
            for ingredient in cocktail[1]:
                if ingredient in self.parent().available_ingredients:
                    n += 1
            if n == len(cocktail[1]):
                self.parent().available_cocktails.append(cocktail)
        self.parent().create_drink_list()
        self.hide()

    def pump_start(self):
        msg = "F" + str(self.number_button(self.parent().name_clicked)) + ";"
        if not self.parent().serial.isOpen():
            print("No Serial. Sending: " + msg)
        else:
            self.parent().serial.write(msg.encode())

    def pump_stop(self):
        if not self.parent().serial.isOpen():
            print("No Serial. Sending: S;")
        else:
            self.parent().serial.write("S;".encode())

    def purge_start(self):
        msg = "R" + str(self.number_button(self.parent().name_clicked)) + ";"
        if not self.parent().serial.isOpen():
            print("No Serial. Sending: " + msg)
        else:
            self.parent().serial.write(msg.encode())

    def number_button(self, name):
        pump = 0
        if name == self.parent().name1:
            pump = 1
        elif name == self.parent().name2:
            pump = 2
        elif name == self.parent().name3:
            pump = 3
        elif name == self.parent().name4:
            pump = 4
        elif name == self.parent().name5:
            pump = 5
        elif name == self.parent().name6:
            pump = 6
        return pump
