from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import requests
from ui_addmovie import Ui_AddMovieWindow
from ui_movieshowtimings import Ui_UpdateShowTimingsScreen
import mysql.connector as mc

mydb = mc.connect(
    host="localhost",
    user="root",
    password='Amongoose_123',
    database="cinedeck")


url = f'http://www.omdbapi.com/?apikey=ef7593c3&t=Moonlight&plot=full'
resp = requests.get(url=url)

data = resp.json()
dire = f'CineDeck\assets\.jpg'
res = data['Poster']
response = requests.get(res)
if response.status_code:
    fp = open(r'CineDeck\assets\mlllll.jpg', 'wb')
    fp.write(response.content)


class Ui_StaffHomeScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.addmovwindow = Ui_AddMovieWindow()
        self.updateshowtimings = Ui_UpdateShowTimingsScreen()
        self.setupUi(self)

    def setupUi(self, StaffHomeScreen):
        if not StaffHomeScreen.objectName():
            StaffHomeScreen.setObjectName(u"StaffHomeScreen")
        StaffHomeScreen.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(StaffHomeScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(770, -30, 870, 200))
        self.label.setPixmap(QPixmap(r"CineDeck\assets\logo.svg"))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, -20, 1920, 150))
        self.label_2.setStyleSheet(u"background-color: rgba(128, 0, 0, 1)")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(380, 400, 520, 260))
        self.pushButton.setStyleSheet(
            "QPushButton{font-size: 30pt;background-color: rgba(60, 80, 140, 1)}")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(980, 400, 520, 260))
        self.pushButton_2.setStyleSheet(
            "QPushButton{font-size: 30pt;background-color: rgba(60, 80, 140, 1)}")
        self.pushButton.clicked.connect(self.openaddmovie)
        self.pushButton_2.clicked.connect(self.openupdatetime)
        StaffHomeScreen.setCentralWidget(self.centralwidget)
        self.label_2.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()

        self.retranslateUi(StaffHomeScreen)

        QMetaObject.connectSlotsByName(StaffHomeScreen)
    # setupUi

    def openaddmovie(self):
        self.addmovwindow.setupUi(self)

    def openupdatetime(self):
        self.updateshowtimings.setupUi(self)

    def retranslateUi(self, StaffHomeScreen):
        StaffHomeScreen.setWindowTitle(QCoreApplication.translate(
            "StaffHomeScreen", u"StaffHomeScreen", None))
        self.label.setText("")
        self.label_2.setText("")
        self.pushButton.setText(QCoreApplication.translate(
            "StaffHomeScreen", u"ADD NEW SHOW", None))
        self.pushButton_2.setText(QCoreApplication.translate(
            "StaffHomeScreen", u"UPDATE SHOWS", None))

    # retranslateUi
