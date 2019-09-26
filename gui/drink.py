#!/usr/bin/env python3

from ui_drink import Ui_Dialog
from PyQt5.QtWidgets import QDialog


class DrinkDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        Ui_Dialog.__init__(self)
        self.setupUi(self)
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.list.insertItems(1, ["Water", "Beer"])
        self.ok.clicked.connect(self.change_drink)
        # self.pump.pressed.connect(self.pump_start)
        # self.pump.released.connect(self.pump_stop)
        # self.purge.pressed.connect(self.purge_start)
        # self.purge.pressed.connect(self.purge_stop)

    def change_drink(self):
        if self.list.currentText() == "Beer":
            print("test")
            self.parent().button_clicked.setStyleSheet("background-image: url(:/Logo/test.png);")
            self.parent().name_clicked.setText("Test")
        self.hide()
