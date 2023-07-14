from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import mysql.connector as mc

from ui_movieinfo import *

import json
f = open(r'CineDeck\vari.json')

f = open(r'CineDeck\vari.json')

x = json.load(f)['movname']

mydb = mc.connect(
	host="localhost",
	user="root",
	password='Amongoose_123',
	database="cinedeck")

cur = mydb.cursor()
q = "SELECT movie_name, movie_poster from movies"
cur.execute(q)
res = cur.fetchall()

class Ui_HomeWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.selfmovieinfo = Ui_MovieInfoWindow()
		self.setupUi(self)

	def openbookingscreen(self):
		if self.sender().objectName() == 'searchmovb':
			movname = self.searchmov.text()
		else:
			sentbutton = self.sender()
			movname = res[int(sentbutton.objectName()[-2:]) if int(sentbutton.objectName()[-2:]) > 9 else int(sentbutton.objectName()[-1])][0]

		dictionary = {
                    "movname": movname,
                }
		with open(r"CineDeck\vari.json", "w") as outfile:
			json.dump(dictionary, outfile)
			outfile.flush()
		self.selfmovieinfo.setupUi(self)


	def setupUi(self, HomeWindow):
		if not HomeWindow.objectName():
			HomeWindow.setObjectName(u"HomeWindow")
		HomeWindow.resize(1920, 1080)
		self.centralwidget = QtWidgets.QWidget(HomeWindow)
		self.centralwidget.setObjectName(u"centralwidget")
		self.label = QLabel(self.centralwidget)
		self.label.setObjectName(u"label")
		self.label.setGeometry(QRect(770, -30, 870, 200))
		self.label.setPixmap(QPixmap(r"CineDeck\assets\logo.svg"))
		self.searchmov = QLineEdit(self.centralwidget)
		self.searchmov.setObjectName(u"searchmov")
		self.searchmov.setGeometry(QRect(1380, 40, 400, 50))
		self.searchmov.setPlaceholderText("Search: ")
		self.searchmov.setStyleSheet("QLineEdit{font-size: 15pt;}")
		self.searchmovb = QPushButton("Go", self.centralwidget)
		self.searchmovb.setObjectName(u"searchmovb")
		self.searchmovb.setGeometry(QRect(1800, 40, 50, 50))
		self.searchmovb.clicked.connect(self.openbookingscreen)
		self.searchmovb.setStyleSheet("QPushButton{font-size: 15pt;}")
		self.label_2 = QLabel(self.centralwidget)
		self.label_2.setObjectName(u"label_2")
		self.label_2.setGeometry(QRect(0, -20, 1920, 150))
		self.label_2.setStyleSheet(u"background-color: rgba(128, 0, 0, 1)")
		self.bg = QLabel(self.centralwidget)
		self.bg.setObjectName(u"bg")
		self.bg.setGeometry(QRect(0, 780, 1920, 1080))
		self.bg.setPixmap(
			QPixmap(r"CineDeck\assets\pure-white-background-85a2a7fd.jpg"))
		group = QButtonGroup()
		for i in range(len(res)):
			if i < 6:
				mov = QPushButton(self.centralwidget)
				group.addButton(mov, i)
				mov.setObjectName(f"mov_0{i}")
				mov.setGeometry(QRect(70 + 307*i, 185, 230, 326))
				mov.setIcon(QIcon("{}".format(res[i][1])))
				mov.setIconSize(QSize(260, 345))
				mov.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
				mov.raise_()
				mov.clicked.connect(self.openbookingscreen)

		for i in range(6, len(res)):
			mov2 = QPushButton(self.centralwidget)
			group.addButton(mov2, i)
			mov2.setObjectName(f"mov_0{i}")

			mov2.setGeometry(QRect(70 + 307*(i-6), 585, 230, 326))

			mov2.setIcon(QIcon("{}".format(res[i][1])))
			mov2.setIconSize(QSize(260, 345))
			mov2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
			mov2.raise_()
			mov2.clicked.connect(self.openbookingscreen)

		HomeWindow.setCentralWidget(self.centralwidget)
		self.bg.raise_()
		self.label_2.raise_()
		self.label.raise_()
		self.searchmov.raise_()
		self.searchmovb.raise_()

		QMetaObject.connectSlotsByName(HomeWindow)

