from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import mysql.connector as mc
from datetime import *
from ui_seats import Ui_SeatsWindow
import json
import PySide2, sys


mydb = mc.connect(
	host="localhost",
	user="root",
	password='Amongoose_123',
	database="cinedeck")

cur = mydb.cursor()

class Ui_MovieBookingWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.seats = Ui_SeatsWindow()
		self.setupUi(self)

	def setupUi(self, MovieBookingWindow):
		MovieBookingWindow.resize(1920, 1080)

		self.n = self.getmovname()

		q = f"SELECT movie_name, movie_poster, movie_desc, movie_price, movie_rating, cast, runtime, director, languages, genre, rated from movies where movie_name = '{self.n}'"
		cur.execute(q)
		res = cur.fetchall()

		q = f"select * from shows where movie_name = '{self.n}'"
		cur.execute(q)
		shows = cur.fetchall()

		for i in res:
			self.movdesc, self.movposter, self.movie_price, self.movie_rating, self.cast, self.runtime, self.director, self.languages, self.genre, self.rated = i[
				2], i[1], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]

		font = QFont()
		font.setFamily(u"Yu Gothic UI Light")
		font.setPointSize(9)
		self.centralwidget = QtWidgets.QWidget(MovieBookingWindow)
		self.centralwidget.setObjectName(u"centralwidget")
		self.label = QLabel(self.centralwidget)
		self.label.setObjectName(u"label")
		self.label.setGeometry(QRect(770, -30, 870, 200))
		self.label.setPixmap(QPixmap(r"CineDeck\assets\logo.svg"))
		self.labe1l = QLabel("Available Showtimings:\nSelect Your Desired Show ", self.centralwidget)
		self.labe1l.setObjectName(u"label")
		self.labe1l.setGeometry(QRect(600, 130, 870, 200))
		self.labe1l.setStyleSheet("QLabel{font-size: 15pt}")
		self.RedHead = QLabel(self.centralwidget)
		self.RedHead.setObjectName(u"RedHead")
		self.RedHead.setGeometry(QRect(0, -20, 1920, 150))
		self.RedHead.setStyleSheet(u"background-color: rgba(128, 0, 0, 1)")
		self.label.raise_()
		self.labe1l.raise_()
		self.movpos = QLabel(self.centralwidget)
		self.movpos.setObjectName(u"movpos")
		self.movpos.setGeometry(QRect(50, 200, 500, 700))
		self.movpos.setPixmap(
			QPixmap(self.movposter))
		self.movpos.setScaledContents(True)
		self.dates = QButtonGroup()

		for i in enumerate(shows):
			showss = QPushButton(
				f"{datetime.strftime(i[1][2], '%d %B, %Y %H:%M:%S')}", self.centralwidget)
			showss.setObjectName(
				f"{datetime.strftime(i[1][2], '%d %B, %Y %H:%M:%S')}")
			showss.setCheckable(True)
			self.dates.addButton(showss)
			showss.raise_()
			if i[0] < 10:
				showss.setGeometry(QRect(600, 300 + 60*i[0], 250, 40))
			if 10 < i[0] < 20:
				showss.setGeometry(QRect(600, 200 + 60*(i[0]-10), 250, 40))
			showss.clicked.connect(self.write)

		self.seatsbutton = QPushButton("BOOK NOW!" ,self.centralwidget)
		self.seatsbutton.setObjectName(u"button")
		self.seatsbutton.setGeometry(QRect(570, 800, 1300, 100))
		self.seatsbutton.setStyleSheet(
			"QPushButton{font-size: 40pt;background-color : rgba(128, 200, 128, 1)}")
		self.seatsbutton.clicked.connect(self.showseats)

		"""self.Title = QLabel(f"{self.n}", self.centralwidget)
		self.Title.setObjectName(u"Title")
		self.Title.setGeometry(QRect(570, 0, 40000, 500))
		self.Title.setStyleSheet("QLabel{font-size: 50pt;}")
		self.Title.setFont(font)"""
		MovieBookingWindow.setCentralWidget(self.centralwidget)
		self.retranslateUi(MovieBookingWindow)

		QMetaObject.connectSlotsByName(MovieBookingWindow)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(QCoreApplication.translate(
			"MainWindow", u"MainWindow", None))
		self.label.setText("")

	def write(self):
		with open(r'CineDeck\show.txt', 'w') as f:
			f.write(str(datetime.strptime(
				self.sender().objectName(), '%d %B, %Y %H:%M:%S')))
			f.flush()

	def showseats(self):
		self.seats.setupUi(self)

	def getmovname(self):
		n = json.load(open(r'CineDeck\vari.json'))['movname']
		return n


if __name__ == "__main__":
    app = PySide2.QtWidgets.QApplication(['bro im doneeee'])
    ex = Ui_MovieBookingWindow()
    ex.show()
    sys.exit(app.exec_())
