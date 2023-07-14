from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import mysql.connector as mc
import sys
import time
import os
from ui_staffhomescreen import Ui_StaffHomeScreen


class Ui_StaffLogInWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.staffdash = Ui_StaffHomeScreen()

    def setupUi(self, StaffLogInWindow):
        if not StaffLogInWindow.objectName():
            StaffLogInWindow.setObjectName(u"StaffLogInWindow")
        StaffLogInWindow.resize(761, 455)
        StaffLogInWindow.setTabShape(QTabWidget.Triangular)
        StaffLogInWindow.setFixedSize(761, 455)
        self.centralwidget = QtWidgets.QWidget(StaffLogInWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(380, -10, 381, 501))
        self.label_6.setPixmap(
            QPixmap(r"CineDeck\assets\pure-white-background-85a2a7fd.jpg"))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 0, 381, 431))
        self.label_7.setPixmap(
            QPixmap(r"CineDeck\assets\download.jpg"))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, -60, 381, 521))
        self.label_8.setStyleSheet(u"background-color: rgba(128, 0, 0, 0.7)")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 120, 311, 181))
        self.label_9.setPixmap(
            QPixmap(r"CineDeck\assets\logo.svg"))
        self.verticalWidget = QWidget(self.centralwidget)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setGeometry(QRect(420, 40, 261, 360))
        self.verticalLayout_2 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.verticalWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Yu Gothic Light")
        font.setPointSize(25)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.verticalWidget)
        self.label_2.setObjectName(u"label_2")
        self.label.setGeometry(QRect(1, 1, 219, 430))
        font1 = QFont()
        font1.setFamily(u"Yu Gothic Light")
        font1.setPointSize(9)
        fontforgot = QFont()
        fontforgot.setFamily(u"Yu Gothic Light")
        fontforgot.setPointSize(7)
        self.label_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.verticalWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.label_3 = QLabel(self.verticalWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.verticalWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.label_4 = QLabel(self.verticalWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(fontforgot)

        self.verticalLayout_2.addWidget(self.label_4)

        self.checkBox = QCheckBox(self.verticalWidget)
        self.checkBox.setObjectName(u"checkBox")
        font2 = QFont()
        font2.setFamily(u"Yu Gothic Light")
        self.checkBox.setFont(font2)

        self.verticalLayout_2.addWidget(self.checkBox)

        self.pushButton = QPushButton(self.verticalWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton.clicked.connect(self.stafflogin)

        StaffLogInWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StaffLogInWindow)

        QMetaObject.connectSlotsByName(StaffLogInWindow)
    # setupUi

    def retranslateUi(self, StaffLogInWindow):
        StaffLogInWindow.setWindowTitle(QCoreApplication.translate(
            "StaffLogInWindow", u"StaffLogInWindow", None))
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_8.setText("")
        self.label_9.setText("")
        self.label.setText(QCoreApplication.translate(
            "StaffLogInWindow", u"Staff Login", None))
        self.label_2.setText(QCoreApplication.translate(
            "StaffLogInWindow", u"Staff ID:", None))
        self.lineEdit.setPlaceholderText(
            QCoreApplication.translate("StaffLogInWindow", u"Enter Staff ID", None))
        self.label_3.setText(QCoreApplication.translate(
            "StaffLogInWindow", u"Password:", None))
        self.lineEdit_2.setPlaceholderText(
            QCoreApplication.translate("StaffLogInWindow", u"Enter Password", None))
        self.label_4.setText(QCoreApplication.translate(
            "StaffLogInWindow", u"Forgot Password?", None))
        self.checkBox.setText(QCoreApplication.translate(
            "StaffLogInWindow", u"Remember Me?", None))
        self.pushButton.setText(
            QCoreApplication.translate("StaffLogInWindow", u"Login", None))
    # retranslateUi

    def stafflogin(self):
        ids = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if ids and password is not None:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password='Amongoose_123',
                database="cinedeck")

            mycursor = mydb.cursor()
            query = f"SELECT staff_id, pass FROM staff_info WHERE staff_id LIKE '{ids}' AND pass LIKE '{password}'"
            mycursor.execute(query)
            result = mycursor.fetchone()

            if result == None:
                QtWidgets.QMessageBox.critical(
                    self, "Error", "Staff ID or Password is incorrect!")

            else:
                QtWidgets.QMessageBox.information(
                    self, "Success ✅", "You Have Been Logged In!")
                self.staffdash.show()

        else:
            QtWidgets.QMessageBox.information(
                self, "Error ", "Please Enter Staff ID or Password.")
