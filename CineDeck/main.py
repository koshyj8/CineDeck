import sys
import PySide2
from PySide2 import QtWidgets, QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from ui_loginscreen import Ui_LogInWindow
from ui_signupscreen import Ui_SignUpWindow
from ui_staffloginscreen import Ui_StaffLogInWindow
from ui_homescreen import *

from datetime import datetime
import mysql.connector as mc

mydb = mc.connect(
    host="localhost",
    user="root",
    password='Amongoose_123',
    database="cinedeck")

cur = mydb.cursor()
now = datetime.now()
timer = datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
cur.execute(f"DELETE from shows where showtimings < '{timer}'")
cur.execute(f"DELETE from halls where showtimings < '{timer}'")
mydb.commit()
mydb.close()


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.selfsignupwindow = Ui_SignUpWindow()
        self.selfloginwindow = Ui_LogInWindow()
        self.selfstaffloginwindow = Ui_StaffLogInWindow()
        self.selfhomewindow = Ui_HomeWindow()

    def setupUi(self, MainWindow):
        MainWindow.resize(790, 495)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-4, 0, 911, 551))
        self.label.setPixmap(
            QPixmap(r"CineDeck\assets\download.jpg"))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(-4, 0, 911, 551))
        self.label_2.setStyleSheet(u"background-color: rgba(128, 0, 0, 0.7)")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 150, 301, 121))
        self.label_3.setPixmap(QPixmap(r"CineDeck\assets\logo.svg"))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(370, 230, 171, 16))
        font = QFont()
        font.setFamily(u"Yu Gothic UI Light")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color : #ffffff;")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(270, 260, 261, 23))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(270, 290, 261, 23))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(500, 450, 261, 23))
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton_3.clicked.connect(self.openstaffloginscreen)
        self.pushButton_2.clicked.connect(self.openloginscreen)
        self.pushButton.clicked.connect(self.opensignupscreen)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.pushButton_2.setText(QCoreApplication.translate(
            "MainWindow", u"Already Have An Account? Log In!", None))
        self.pushButton.setText(QCoreApplication.translate(
            "MainWindow", u"New To CineDeck? Sign Up", None))
        self.pushButton_3.setText(QCoreApplication.translate(
            "MainWindow", u"Staff Member Login", None
        ))

    def opensignupscreen(self):
        self.selfsignupwindow.setupUi(self)

    def openstaffloginscreen(self):
        self.selfstaffloginwindow.setupUi(self)
        with open(r'CineDeck\prevwindow.txt', 'w') as fh:
            fh.write(str(self.selfstaffloginwindow).split('<')[1].split(' o')[0])

    def openloginscreen(self):
        self.selfloginwindow.setupUi(self)
        with open(r'CineDeck\prevwindow.txt', 'w') as fh:
            fh.write(str(self.selfloginwindow).split('<')[1].split(' o')[0])

if __name__ == "__main__":
    app = PySide2.QtWidgets.QApplication(['bro im doneeee'])
    pixmap = QPixmap(r"CineDeck\assets\logo.svg")
    splash = QSplashScreen(pixmap)
    splash.show()
    #time.sleep(5)
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(app.exec_())
