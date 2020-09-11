from ui.py.ui_finished import Ui_Finished
from PyQt5 import QtWidgets


class FinishedDialog(QtWidgets.QDialog, Ui_Finished):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        Ui_Finished.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Boisson finie!")
        self.newDrink.clicked.connect(self.back)

    def back(self):
        self.hide()
        self.parent().hide()
