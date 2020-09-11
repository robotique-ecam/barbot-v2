#!/usr/bin/env python3

from ui.py.ui_drink import Ui_Drink
from PyQt5.QtWidgets import QDialog
# from PyQt5 import QtGui


class DrinkDialog(QDialog, Ui_Drink):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        Ui_Drink.__init__(self)
        self.setupUi(self)
        self.ok.clicked.connect(self.update_drinks)
        self.pump.pressed.connect(self.pump_start)
        self.pump.released.connect(self.stop)
        self.purge.pressed.connect(self.purge_start)
        self.purge.released.connect(self.stop)

    def update_drinks(self):
        """Updating image and name of ingredient on the admin tab."""
        self.parent().name_clicked.setText(self.list.currentText())
        # for drink in self.parent().cocktails:
        #     if drink[0] == self.parent().name_clicked.text():
        #         self.parent().name_clicked.setFont(QtGui.QFont("Verdana", drink[2] / 2))
        # self.parent().button_clicked.setStyleSheet("background-image: url(:/Logo/" + cocktails[self.list.currentText()[2]] + ".png)")
        self.parent().parent().set_saved_ingredients()
        self.parent().parent().update_drink_list()
        self.hide()

    def pump_start(self):
        msg = f"F{self.number_button(self.parent().name_clicked)};"
        if not self.parent().parent().serial.isOpen():
            print(f"No Serial. Sending: {msg}")
        else:
            self.parent().parent().serial.write(msg.encode())

    def stop(self):
        if not self.parent().parent().serial.isOpen():
            print("No Serial. Sending: S;")
        else:
            self.parent().parent().serial.write("S;".encode())

    def purge_start(self):
        msg = f"R{self.number_button(self.parent().name_clicked)};"
        if not self.parent().parent().serial.isOpen():
            print(f"No Serial. Sending: {msg}")
        else:
            self.parent().parent().serial.write(msg.encode())

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
