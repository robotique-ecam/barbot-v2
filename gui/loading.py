from ui.py.ui_loading import Ui_Loading
from finished import FinishedDialog
from PyQt5 import QtTest
from PyQt5.QtWidgets import QDialog


class LoadingDialog(QDialog, Ui_Loading):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        Ui_Loading.__init__(self)
        self.setupUi(self)
        self.finishedDialog = FinishedDialog(self)

    def manual(self):
        """Used only when no serial is detected, function for testing purposes."""
        QtTest.QTest.qWait(3000)
        # self.gif_gobelet.stop()
        for key, value in self.parent().ing_dict.items():
            if key == self.parent().settingsDialog.name1.text():
                pump = 1
            elif key == self.parent().settingsDialog.name2.text():
                pump = 2
            elif key == self.parent().settingsDialog.name3.text():
                pump = 3
            elif key == self.parent().settingsDialog.name4.text():
                pump = 4
            elif key == self.parent().settingsDialog.name5.text():
                pump = 5
            elif key == self.parent().settingsDialog.name6.text():
                pump = 6
            self.parent().gif_conveyor.start()
            self.step.setText(f"Moving carpet to position {pump}")
            print(f"No serial. Sending: C{pump};")
            QtTest.QTest.qWait(3000)
            self.parent().gif_conveyor.stop()
            self.parent().gif_glass.start()
            self.step.setText(f"Pumping at position {pump}")
            print(f"No serial. Sending: P{pump}-{value};")
            QtTest.QTest.qWait(3000)
            self.parent().gif_glass.stop()
        self.parent().gif_conveyor.start()
        self.step.setText("Moving carpet to the end")
        print("No serial. Sending: End;")
        QtTest.QTest.qWait(3000)
        self.parent().gif_conveyor.stop()
        self.finishedDialog.setModal(True)
        self.finishedDialog.show()
