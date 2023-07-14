from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import PySide2, sys
from ui_homescreen import *

import mysql.connector as mc
import time


class Ui_LogInWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.selfhomewindow = Ui_HomeWindow()
        self.setupUi(self)

    def setupUi(self, LogInWindow):
        if not LogInWindow.objectName():
            LogInWindow.setObjectName(u"LogInWindow")
        LogInWindow.resize(761, 455)
        self.centralwidget = QtWidgets.QWidget(LogInWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(380, -10, 381, 501))
        self.label_6.setPixmap(
            QPixmap(r"CineDeck\assets\pure-white-background-85a2a7fd.jpg"))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 0, 381, 500))
        self.label_7.setPixmap(
            QPixmap(r"CineDeck\assets\download.jpg"))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, -60, 381, 521))
        self.label_8.setStyleSheet(u"background-color: rgba(128, 0, 0, 0.7)")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 120, 311, 181))
        self.label_9.setPixmap(QPixmap(r"CineDeck\assets\logo.svg"))
        self.verticalWidget = QWidget(self.centralwidget)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setGeometry(QRect(470, 40, 221, 360))
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
        self.label_2.setGeometry(QRect(1, 1, 219, 430))
        font1 = QFont()
        font1.setFamily(u"Yu Gothic Light")
        font1.setPointSize(9)
        self.label_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_2)

        self.emailLineEdit = QLineEdit(self.verticalWidget)
        self.emailLineEdit.setObjectName(u"emailLineEdit")
        self.emailLineEdit.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.emailLineEdit)

        self.label_3 = QLabel(self.verticalWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.passwordLineEdit = QLineEdit(self.verticalWidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setAutoFillBackground(False)
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.passwordLineEdit)

        self.label_4 = QLabel(self.verticalWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_4)

        self.checkBox = QCheckBox(self.verticalWidget)
        self.checkBox.setObjectName(u"checkBox")
        font2 = QFont()
        font2.setFamily(u"Yu Gothic Light")
        self.checkBox.setFont(font2)

        self.verticalLayout_2.addWidget(self.checkBox)

        self.pushButton = QPushButton(self.verticalWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.clicked.connect(self.login)
        self.verticalLayout_2.addWidget(self.pushButton)

        self.label_5 = QLabel(self.verticalWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_5)

        LogInWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LogInWindow)

        QMetaObject.connectSlotsByName(LogInWindow)

    def retranslateUi(self, LogInWindow):
        LogInWindow.setWindowTitle(QCoreApplication.translate(
            "LogInWindow", u"LogInWindow", None))
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_8.setText("")
        self.label_9.setText("")
        self.label.setText(QCoreApplication.translate(
            "LogInWindow", u"Login", None))
        self.label_2.setText(QCoreApplication.translate(
            "LogInWindow", u"Email:", None))
        self.emailLineEdit.setPlaceholderText(
            QCoreApplication.translate("LogInWindow", u"Enter Email", None))
        self.label_3.setText(QCoreApplication.translate(
            "LogInWindow", u"Password:", None))
        self.passwordLineEdit.setPlaceholderText(
            QCoreApplication.translate("LogInWindow", u"Enter Password", None))
        self.label_4.setText(QCoreApplication.translate(
            "LogInWindow", u"Forgot Password?", None))
        self.checkBox.setText(QCoreApplication.translate(
            "LogInWindow", u"Remember Me?", None))
        self.pushButton.setText(
            QCoreApplication.translate("LogInWindow", u"Login", None))
        self.label_5.setText(QCoreApplication.translate(
            "LogInWindow", u"New to CineDeck? Sign Up", None))


    def login(self):
        email = self.emailLineEdit.text()
        password = self.passwordLineEdit.text()
        if email and password is not None:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password='Amongoose_123',
                database="cinedeck")

            mycursor = mydb.cursor()
            query = f"SELECT email, password FROM user_info WHERE email = '{email}'"
            mycursor.execute(query)
            result = mycursor.fetchone()
            mydb.close()
            if result:
                if result[1] == password:
                    msg = QMessageBox()
                    msg.setText('Successfully Logged into Cinedeck!')
                    with open(r'CineDeck\username.txt', 'w') as f:
                        f.write(email)
                        f.flush()
                    #time.sleep(5)
                    self.selfhomewindow.show()

                else:
                    QMessageBox.about(self, "Error ⚠️", "Incorrect Password!")

            else:
                QMessageBox.about(self, "Error ⚠️", "Account does not exist!")
        else:
            QMessageBox.about(
                self, "Error ", "Please Enter Email or Password.")

