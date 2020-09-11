from ui.py.ui_settings import Ui_Settings
from drink import DrinkDialog
from cocktails import cocktails
from PyQt5.QtWidgets import QDialog


class SettingsDialog(QDialog, Ui_Settings):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        Ui_Settings.__init__(self)
        self.setupUi(self)
        self.create_ingredients()
        self.menuButton.clicked.connect(self.hide)
        self.picture1.clicked.connect(lambda: self.open_drink(self.picture1))
        self.picture2.clicked.connect(lambda: self.open_drink(self.picture2))
        self.picture3.clicked.connect(lambda: self.open_drink(self.picture3))
        self.picture4.clicked.connect(lambda: self.open_drink(self.picture4))
        self.picture5.clicked.connect(lambda: self.open_drink(self.picture5))
        self.picture6.clicked.connect(lambda: self.open_drink(self.picture6))
        self.name1.setText(self.parent().current_ingredients[0])
        self.name2.setText(self.parent().current_ingredients[1])
        self.name3.setText(self.parent().current_ingredients[2])
        self.name4.setText(self.parent().current_ingredients[3])
        self.name5.setText(self.parent().current_ingredients[4])
        self.name6.setText(self.parent().current_ingredients[5])
        self.carpet_left.pressed.connect(self.carpet_left_start)
        self.carpet_left.released.connect(self.carpet_stop)
        self.carpet_right.pressed.connect(self.carpet_right_start)
        self.carpet_right.released.connect(self.carpet_stop)
        self.gobelet.clicked.connect(self.gobelet_push)

    def open_drink(self, button):
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
        self.drinkDialog = DrinkDialog(self)
        self.drinkDialog.list.insertItems(1, [' '] + self.ingredients)
        self.drinkDialog.list.setCurrentText(self.name_clicked.text())
        self.drinkDialog.name.setText(self.name_clicked.text())
        self.drinkDialog.setModal(True)
        self.drinkDialog.show()

    def create_ingredients(self):
        self.ingredients = []
        for name, cocktail_info in cocktails.items():
            self.ingredients += [ing for ing in cocktail_info[0].keys() if ing not in self.ingredients]

    def carpet_left_start(self):
        if not self.parent().serial.isOpen():
            print("No Serial. Sending: RC;")
        else:
            self.parent().serial.write("RC;".encode())

    def carpet_right_start(self):
        if not self.parent().serial.isOpen():
            print("No Serial. Sending: FC;")
        else:
            self.parent().serial.write("FC;".encode())

    def carpet_stop(self):
        if not self.parent().serial.isOpen():
            print("No Serial. Sending: S;")
        else:
            self.parent().serial.write("S;".encode())

    def gobelet_push(self):
        if not self.parent().serial.isOpen():
            print("No Serial. Sending: FG;")
        else:
            self.parent().serial.write("FG;".encode())
