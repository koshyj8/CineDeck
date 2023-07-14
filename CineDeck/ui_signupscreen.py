from PySide2 import QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import mysql.connector as mc
from ui_homescreen import Ui_HomeWindow
from ui_loginscreen import Ui_LogInWindow


class Ui_SignUpWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.selfhomewindow = Ui_HomeWindow()
        self.selfloginwindow = Ui_LogInWindow()

    def openhomescreen(self):
        self.selfhomewindow.setupUi(self)

    def setupUi(self, SignUpWindow):
        if not SignUpWindow.objectName():
            SignUpWindow.setObjectName(u"SignUpWindow")
        SignUpWindow.resize(761, 455)
        SignUpWindow.setFixedSize(761, 455)
        self.centralwidget = QtWidgets.QWidget(SignUpWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(380, -10, 391, 501))
        self.label_6.setPixmap(
            QPixmap(r"CineDeck\assets\pure-white-background-85a2a7fd.jpg"))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 0, 391, 521))
        self.label_8.setStyleSheet(u"background-color: rgba(128, 0, 0, 0.8)")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 180, 311, 181))
        self.label_9.setPixmap(
            QPixmap(r"CineDeck\assets\logo.svg"))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 0, 391, 450))
        self.label_7.setPixmap(
            QPixmap(r"CineDeck\assets\download.jpg"))
        self.verticalWidget = QWidget(self.centralwidget)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setGeometry(QRect(420, 20, 280, 400))
        self.verticalLayout = QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.verticalWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Yu Gothic Light")
        font.setPointSize(25)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.verticalWidget)
        self.label_2.setObjectName(u"label_2")

        font1 = QFont()
        font1.setFamily(u"Yu Gothic Light")
        font1.setPointSize(9)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.nameEdit = QLineEdit(self.verticalWidget)
        self.nameEdit.setObjectName(u"nameEdit")
        self.nameEdit.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.nameEdit)

        self.label_10 = QLabel(self.verticalWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.verticalLayout.addWidget(self.label_10)

        self.emailEdit = QLineEdit(self.verticalWidget)
        self.emailEdit.setObjectName(u"emailEdit")
        self.emailEdit.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.emailEdit)

        self.label_3 = QLabel(self.verticalWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.verticalWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.verticalLayout.addWidget(self.label_4)

        self.passwordEdit = QLineEdit(self.verticalWidget)
        self.passwordEdit.setObjectName(u"passwordEdit")
        self.passwordEdit.setAutoFillBackground(False)
        self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.passwordEdit)

        self.label_5 = QLabel(self.verticalWidget)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setFamily(u"Yu Gothic Light")
        self.label_5.setFont(font2)

        self.verticalLayout.addWidget(self.label_5)

        self.pushButton = QPushButton(self.verticalWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        SignUpWindow.setCentralWidget(self.centralwidget)
        self.label_7.raise_()
        self.label_6.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.verticalWidget.raise_()
        self.menubar = QMenuBar(SignUpWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 761, 22))
        SignUpWindow.setMenuBar(self.menubar)

        self.pushButton.clicked.connect(self.createacc)
        self.retranslateUi(SignUpWindow)

        QMetaObject.connectSlotsByName(SignUpWindow)
    # setupUi

    def retranslateUi(self, SignUpWindow):
        SignUpWindow.setWindowTitle(QCoreApplication.translate(
            "SignUpWindow", u"SignUpWindow", None))
        self.label_6.setText("")
        self.label_8.setText("")
        self.label_9.setText("")
        self.label_7.setText("")
        self.label.setText(QCoreApplication.translate(
            "SignUpWindow", u"Sign Up", None))
        self.label_2.setText(QCoreApplication.translate(
            "SignUpWindow", u"Name:", None))

        self.nameEdit.setText("")
        self.nameEdit.setPlaceholderText(
            QCoreApplication.translate("SignUpWindow", u"Enter Name", None))

        self.label_10.setText(QCoreApplication.translate(
            "SignUpWindow", u"Email:", None))
        self.emailEdit.setText("")
        self.emailEdit.setPlaceholderText(
            QCoreApplication.translate("SignUpWindow", u"Enter Email", None))
        self.label_3.setText(QCoreApplication.translate(
            "SignUpWindow", u"Password:", None))
        self.passwordEdit.setPlaceholderText(
            QCoreApplication.translate("SignUpWindow", u"Enter Password", None))
        self.label_5.setText(QCoreApplication.translate(
            "SignUpWindow", u"Already have an account? Log In", None))
        self.pushButton.setText(QCoreApplication.translate(
            "SignUpWindow", u"Sign Up", None))
    # retranslateUi

    def createacc(self):
        name = self.nameEdit.text()

        password = self.passwordEdit.text()
        email = self.emailEdit.text()
        if name and password and email is not None:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password='Amongoose_123',
                database="cinedeck")
            mycursor = mydb.cursor()
            query = f"SELECT name, email from user_info where email LIKE '{email}'"
            mycursor.execute(query)
            result = mycursor.fetchone()
            if result:
                QMessageBox.about(
                    self, "Error", "Account with this email already exists.")
            else:
                insert = f"INSERT INTO user_info (password, name, email) VALUES ('{password}', '{name}', '{email}')"
                mycursor.execute(insert)
                mydb.commit()
                mydb.close()
                QMessageBox.information(
                    self, "Success ✅", "Successfully created CineDeck Account!")
                with open(r'CineDeck\username.txt', 'w') as f:
                    f.write(email)
                    f.flush()
                self.selfhomewindow.show()
                self.close()

        else:
            QtWidgets.QMessageBox.critical(
                self, "Error", "Please Enter Details!")
