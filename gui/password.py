#!/usr/bin/env python3

from PyQt5 import QtTest
from ui_password import Ui_Dialog
from PyQt5.QtWidgets import QDialog


class PasswordDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        Ui_Dialog.__init__(self)
        self.setupUi(self)
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
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
        if self.lineEdit.text() == "8192":
            self.lineEdit.setText("")
            self.hide()
            self.parent().tabWidget.setCurrentIndex(3)
        elif self.lineEdit.text() == "4096":
            if self.parent().night_mode:
                self.parent().night_mode = False
                self.parent().create_ingredients()
            else:
                self.parent().night_mode = True
                self.parent().create_ingredients()
            self.lineEdit.setText("")
            self.hide()
        else:
            self.lineEdit.setText("Wrong!")
            QtTest.QTest.qWait(1000)
            self.lineEdit.setText("")

    def erasing(self):
        if len(self.lineEdit.text()) > 0:
            self.lineEdit.setText(self.lineEdit.text()[:-1])
        else:
            self.hide()
