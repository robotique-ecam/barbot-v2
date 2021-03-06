# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui/settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(1024, 600)
        self.name4 = QtWidgets.QLineEdit(Settings)
        self.name4.setGeometry(QtCore.QRect(510, 290, 162, 58))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name4.sizePolicy().hasHeightForWidth())
        self.name4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.name4.setFont(font)
        self.name4.setStyleSheet("border-right: 5px solid;\n"
"border-left: 5px solid;\n"
"border-bottom: 5px solid;")
        self.name4.setText("")
        self.name4.setFrame(False)
        self.name4.setAlignment(QtCore.Qt.AlignCenter)
        self.name4.setReadOnly(True)
        self.name4.setObjectName("name4")
        self.name3 = QtWidgets.QLineEdit(Settings)
        self.name3.setGeometry(QtCore.QRect(340, 290, 162, 58))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name3.sizePolicy().hasHeightForWidth())
        self.name3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.name3.setFont(font)
        self.name3.setStyleSheet("border-right: 5px solid;\n"
"border-left: 5px solid;\n"
"border-bottom: 5px solid;")
        self.name3.setText("")
        self.name3.setFrame(False)
        self.name3.setAlignment(QtCore.Qt.AlignCenter)
        self.name3.setReadOnly(True)
        self.name3.setObjectName("name3")
        self.picture2 = QtWidgets.QPushButton(Settings)
        self.picture2.setGeometry(QtCore.QRect(170, 120, 162, 162))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.picture2.sizePolicy().hasHeightForWidth())
        self.picture2.setSizePolicy(sizePolicy)
        self.picture2.setText("")
        self.picture2.setIconSize(QtCore.QSize(165, 165))
        self.picture2.setCheckable(False)
        self.picture2.setDefault(False)
        self.picture2.setFlat(True)
        self.picture2.setObjectName("picture2")
        self.picture6 = QtWidgets.QPushButton(Settings)
        self.picture6.setGeometry(QtCore.QRect(850, 120, 162, 162))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.picture6.sizePolicy().hasHeightForWidth())
        self.picture6.setSizePolicy(sizePolicy)
        self.picture6.setStyleSheet("border-right: 5px solid;\n"
"border-left: 5px solid;")
        self.picture6.setText("")
        self.picture6.setIconSize(QtCore.QSize(165, 165))
        self.picture6.setCheckable(False)
        self.picture6.setDefault(False)
        self.picture6.setFlat(True)
        self.picture6.setObjectName("picture6")
        self.name2 = QtWidgets.QLineEdit(Settings)
        self.name2.setGeometry(QtCore.QRect(170, 290, 162, 58))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name2.sizePolicy().hasHeightForWidth())
        self.name2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.name2.setFont(font)
        self.name2.setStyleSheet("border-right: 5px solid;\n"
"border-left: 5px solid;\n"
"border-bottom: 5px solid;")
        self.name2.setText("")
        self.name2.setFrame(False)
        self.name2.setAlignment(QtCore.Qt.AlignCenter)
        self.name2.setReadOnly(True)
        self.name2.setObjectName("name2")
        self.menuButton = QtWidgets.QPushButton(Settings)
        self.menuButton.setGeometry(QtCore.QRect(10, 540, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.menuButton.setFont(font)
        self.menuButton.setObjectName("menuButton")
        self.line2 = QtWidgets.QLineEdit(Settings)
        self.line2.setGeometry(QtCore.QRect(170, 71, 162, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line2.sizePolicy().hasHeightForWidth())
        self.line2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.line2.setFont(font)
        self.line2.setStyleSheet("border-right: 5px solid;\n"
"border-left: 5px solid;\n"
"border-top: 5px solid;")
        self.line2.setFrame(False)
        self.line2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.line2.setDragEnabled(False)
        self.line2.setReadOnly(True)
        self.line2.setObjectName("line2")
        self.carpet_right = QtWidgets.QPushButton(Settings)
        self.carpet_right.setGeometry(QtCore.QRect(518, 400, 161, 151))
        self.carpet_right.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Logo/arrow_right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.carpet_right.setIcon(icon)
        self.carpet_right.setIconSize(QtCore.QSize(150, 150))
        self.carpet_right.setObjectName("carpet_right")
        self.picture1 = QtWidgets.QPushButton(Settings)
        self.picture1.setGeometry(QtCore.QRect(1, 120, 162, 162))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.picture1.sizePolicy().hasHeightForWidth())
        self.picture1.setSizePolicy(sizePolicy)
        self.picture1.setStyleSheet("")
        self.picture1.setText("")
        self.picture1.setIconSize(QtCore.QSize(165, 165))
        self.picture1.setCheckable(False)
        self.picture1.setDefault(False)
        self.picture1.setFlat(True)
        self.picture1.setObjectName("picture1")
        self.picture4 = QtWidgets.QPushButton(Settings)
        self.picture4.setGeometry(QtCore.QRect(510, 120, 162, 162))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.picture4.sizePolicy().hasHeightForWidth())
        self.picture4.setSizePolicy(sizePolicy)
        self.picture4.setText("")
        self.picture4.setIconSize(QtCore.QSize(165, 165))
        self.picture4.setCheckable(False)
        self.picture4.setDefault(False)
        self.picture4.setFlat(True)
        self.picture4.setObjectName("picture4")
        self.line5 = QtWidgets.QLineEdit(Settings)
        self.line5.setGeometry(QtCore.QRect(680, 71, 162, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line5.sizePolicy().hasHeightForWidth())
        self.line5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.line5.setFont(font)
        self.line5.setStyleSheet("border-right: 5px solid;\n"
"border-left: 5px solid;\n"
"border-top: 5px solid;")
        self.line5.setFrame(False)
        self.line5.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.line5.setDragEnabled(False)
        self.line5.setReadOnly(True)
        self.line5.setObjectName("line5")
        self.carpet_left = QtWidgets.QPushButton(Settings)
        self.carpet_left.setGeometry(QtCore.QRect(345, 400, 161, 151))
        self.carpet_left.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Logo/arrow_left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.carpet_left.setIcon(icon1)
        self.carpet_left.setIconSize(QtCore.QSize(150, 150))
        self.carpet_left.setObjectName("carpet_left")
        self.name1 = QtWidgets.QLineEdit(Settings)
        self.name1.setGeometry(QtCore.QRect(1, 290, 162, 58))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name1.sizePolicy().hasHeightForWidth())
        self.name1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.name1.setFont(font)
        self.name1.setStyleSheet("border-right: 5px solid;\n"
"border-left: 5px solid;\n"
"border-bottom: 5px solid;")
        self.name1.setText("")
        self.name1.setFrame(False)
        self.name1.setAlignment(QtCore.Qt.AlignCenter)
        self.name1.setReadOnly(True)
        self.name1.setObjectName("name1")
        self.line3 = QtWidgets.QLineEdit(Settings)
        self.line3.setGeometry(QtCore.QRect(340, 71, 162, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line3.sizePolicy().hasHeightForWidth())
        self.line3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.line3.setFont(font)
        self.line3.setStyleSheet("border-right: 5px solid;\n"
"border-left: 5px solid;\n"
"border-top: 5px solid;")
        self.line3.setFrame(False)
        self.line3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.line3.setDragEnabled(False)
        self.line3.setReadOnly(True)
        self.line3.setObjectName("line3")
        self.name5 = QtWidgets.QLineEdit(Settings)
        self.name5.setGeometry(QtCore.QRect(680, 290, 162, 58))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name5.sizePolicy().hasHeightForWidth())
        self.name5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.name5.setFont(font)
        self.name5.setStyleSheet("border-right: 5px solid;\n"
"border-left: 5px solid;\n"
"border-bottom: 5px solid;")
        self.name5.setText("")
        self.name5.setFrame(False)
        self.name5.setAlignment(QtCore.Qt.AlignCenter)
        self.name5.setReadOnly(True)
        self.name5.setObjectName("name5")
        self.picture5 = QtWidgets.QPushButton(Settings)
        self.picture5.setGeometry(QtCore.QRect(680, 120, 162, 162))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.picture5.sizePolicy().hasHeightForWidth())
        self.picture5.setSizePolicy(sizePolicy)
        self.picture5.setText("")
        self.picture5.setIconSize(QtCore.QSize(165, 165))
        self.picture5.setCheckable(False)
        self.picture5.setDefault(False)
        self.picture5.setFlat(True)
        self.picture5.setObjectName("picture5")
        self.picture3 = QtWidgets.QPushButton(Settings)
        self.picture3.setGeometry(QtCore.QRect(340, 120, 162, 162))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.picture3.sizePolicy().hasHeightForWidth())
        self.picture3.setSizePolicy(sizePolicy)
        self.picture3.setText("")
        self.picture3.setIconSize(QtCore.QSize(165, 165))
        self.picture3.setCheckable(False)
        self.picture3.setDefault(False)
        self.picture3.setFlat(True)
        self.picture3.setObjectName("picture3")
        self.line1 = QtWidgets.QLineEdit(Settings)
        self.line1.setGeometry(QtCore.QRect(1, 71, 162, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line1.sizePolicy().hasHeightForWidth())
        self.line1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.line1.setFont(font)
        self.line1.setStyleSheet("border-right: 5px solid;\n"
"border-left: 5px solid;\n"
"border-top: 5px solid;")
        self.line1.setFrame(False)
        self.line1.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.line1.setDragEnabled(False)
        self.line1.setReadOnly(True)
        self.line1.setObjectName("line1")
        self.gobelet = QtWidgets.QPushButton(Settings)
        self.gobelet.setGeometry(QtCore.QRect(850, 400, 161, 151))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.gobelet.setFont(font)
        self.gobelet.setIconSize(QtCore.QSize(150, 150))
        self.gobelet.setObjectName("gobelet")
        self.name6 = QtWidgets.QLineEdit(Settings)
        self.name6.setGeometry(QtCore.QRect(850, 290, 162, 58))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name6.sizePolicy().hasHeightForWidth())
        self.name6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.name6.setFont(font)
        self.name6.setStyleSheet("border-right: 5px solid;\n"
"border-left: 5px solid;\n"
"border-bottom: 5px solid;")
        self.name6.setText("")
        self.name6.setFrame(False)
        self.name6.setAlignment(QtCore.Qt.AlignCenter)
        self.name6.setReadOnly(True)
        self.name6.setObjectName("name6")
        self.line4 = QtWidgets.QLineEdit(Settings)
        self.line4.setGeometry(QtCore.QRect(510, 71, 162, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line4.sizePolicy().hasHeightForWidth())
        self.line4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.line4.setFont(font)
        self.line4.setStyleSheet("border-right: 5px solid;\n"
"border-left: 5px solid;\n"
"border-top: 5px solid;")
        self.line4.setFrame(False)
        self.line4.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.line4.setDragEnabled(False)
        self.line4.setReadOnly(True)
        self.line4.setObjectName("line4")
        self.line6 = QtWidgets.QLineEdit(Settings)
        self.line6.setGeometry(QtCore.QRect(850, 71, 162, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line6.sizePolicy().hasHeightForWidth())
        self.line6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.line6.setFont(font)
        self.line6.setStyleSheet("border-right: 5px solid;\n"
"border-left: 5px solid;\n"
"border-top: 5px solid;")
        self.line6.setFrame(False)
        self.line6.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.line6.setDragEnabled(False)
        self.line6.setReadOnly(True)
        self.line6.setObjectName("line6")
        self.name4.raise_()
        self.name3.raise_()
        self.name2.raise_()
        self.menuButton.raise_()
        self.line2.raise_()
        self.carpet_right.raise_()
        self.line5.raise_()
        self.carpet_left.raise_()
        self.name1.raise_()
        self.line3.raise_()
        self.name5.raise_()
        self.line1.raise_()
        self.gobelet.raise_()
        self.name6.raise_()
        self.line4.raise_()
        self.line6.raise_()
        self.picture2.raise_()
        self.picture5.raise_()
        self.picture1.raise_()
        self.picture3.raise_()
        self.picture4.raise_()
        self.picture6.raise_()

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Dialog"))
        self.menuButton.setText(_translate("Settings", "Menu"))
        self.line2.setText(_translate("Settings", "2"))
        self.line5.setText(_translate("Settings", "5"))
        self.line3.setText(_translate("Settings", "3"))
        self.line1.setText(_translate("Settings", "1"))
        self.gobelet.setText(_translate("Settings", "Gobelet"))
        self.line4.setText(_translate("Settings", "4"))
        self.line6.setText(_translate("Settings", "6"))
import resources_rc
