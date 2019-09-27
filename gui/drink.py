#!/usr/bin/env python3

from ui_drink import Ui_Dialog
from PyQt5.QtWidgets import QDialog


class DrinkDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        Ui_Dialog.__init__(self)
        self.setupUi(self)
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.list.insertItems(1, [" ", "Water", "Beer"])
        self.ok.clicked.connect(self.change_drink)
        self.pump.pressed.connect(self.pump_start)
        self.pump.released.connect(self.pump_stop)
        self.purge.pressed.connect(self.purge_start)
        self.purge.pressed.connect(self.purge_stop)

    def change_drink(self):
        if self.list.currentText() == " ":
            self.parent().button_clicked.setStyleSheet("")
            self.parent().name_clicked.setText("")
        elif self.list.currentText() == "Water":
            self.parent().button_clicked.setStyleSheet("background-image: url(:/Logo/test.png);")
            self.parent().name_clicked.setText("Water")
        elif self.list.currentText() == "Beer":
            self.parent().button_clicked.setStyleSheet("background-image: url(:/Logo/test.png);")
            self.parent().name_clicked.setText("Beer")
        self.parent().available_drinks = [self.parent().name1.text(), self.parent().name2.text(), self.parent().name3.text(), self.parent().name4.text(), self.parent().name5.text(), self.parent().name6.text()]
        for cocktail in self.parent().cocktails:
            n = 0
            for drink in cocktail[1]:
                if drink in self.parent().available_drinks:
                    n += 1
            if n == len(cocktail[1]):
                if cocktail not in self.parent().available_cocktails:
                    self.parent().available_cocktails.append(cocktail)
            elif n != len(cocktail[1]) and cocktail in self.parent().available_cocktails:
                self.parent().available_cocktails.remove(cocktail)
        for avail in self.parent().available_cocktails:
            print(avail[0])
        print("\n")
        self.hide()

    def pump_start(self):
        pass
        # Start pump

    def pump_stop(self):
        pass
        # ...

    def purge_start(self):
        pass
        # ...

    def purge_stop(self):
        pass
        # ...
