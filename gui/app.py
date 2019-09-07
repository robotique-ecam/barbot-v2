#!/usr/bin/env python3


"""This is your app docstring."""


import sys
from PyQt5 import QtCore
from ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication


if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class MainWindow(QMainWindow, Ui_MainWindow):

    """Main board edition window."""

    def __init__(self):
        """Init."""
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
