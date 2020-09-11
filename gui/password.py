#!/usr/bin/env python3

from PyQt5 import QtTest
from ui.py.ui_password import Ui_Password
from PyQt5.QtWidgets import QDialog


class PasswordDialog(QDialog, Ui_Password):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        Ui_Password.__init__(self)
        self.setupUi(self)
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
        if len(self.lineEdit.text()) < 5:
            self.lineEdit.setText(self.lineEdit.text() + button.text())

    def check_password(self):
        if self.lineEdit.text() == "8192":
            self.lineEdit.setText("")
            self.hide()
            self.parent().open_settings()
        else:
            self.lineEdit.setText("Wrong!")
            QtTest.QTest.qWait(1000)
            self.lineEdit.setText("")

    def erasing(self):
        if len(self.lineEdit.text()) > 0:
            self.lineEdit.setText(self.lineEdit.text()[:-1])
        else:
            self.hide()
