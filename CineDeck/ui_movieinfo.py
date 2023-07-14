from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import mysql.connector as mc
from datetime import *
from ui_booking import Ui_MovieBookingWindow
import json
import PySide2, sys

mydb = mc.connect(
	host="localhost",
	user="root",
	password='Amongoose_123',
	database="cinedeck")

cur = mydb.cursor()

class Ui_MovieInfoWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.booking = Ui_MovieBookingWindow()
		self.setupUi(self)

	def openmoviebookingscreen(self):
		self.booking.setupUi(self)

	def setupUi(self, MovieInfoWindow):

		MovieInfoWindow.setObjectName(u"MovieInfoWindow")

		font = QFont()
		font.setFamily(u"Yu Gothic UI Light")
		font.setPointSize(9)

		self.centralwidget = QtWidgets.QWidget(MovieInfoWindow)
		self.centralwidget.setObjectName(u"centralwidget")
		self.label = QLabel(self.centralwidget)
		self.label.setObjectName(u"label")
		self.label.setGeometry(QRect(770, -30, 870, 200))
		self.label.setPixmap(QPixmap(r"CineDeck\assets\logo.svg"))
		self.RedHead = QLabel(self.centralwidget)
		self.RedHead.setObjectName(u"RedHead")
		self.RedHead.setGeometry(QRect(0, -20, 1920, 150))
		self.RedHead.setStyleSheet(u"background-color: rgba(128, 0, 0, 1)")
		#self.showtimes = QLabel((i for i in shows), self.centralwidget)
		#self.showtimes.setGeometry(QRect(1800, -30, 870, 200))
		self.bg = QLabel(self.centralwidget)
		self.bg.setObjectName(u"bg")
		self.bg.setGeometry(QRect(500, 0, 1920, 1080))
		self.n = self.getmovname()


		q = "SELECT movie_name, movie_poster, movie_desc, movie_price, movie_rating, cast, runtime, director, languages, genre, rated from movies"
		cur.execute(q)
		res = cur.fetchall()
		q = f"select showtimings from shows where movie_name = '{self.n}'"
		cur.execute(q)
		shows = cur.fetchall()
		self.dates = []
		present = datetime.now()

		for i in shows:
			if shows.index(i) < 8:
				x = datetime.strftime(i[0], '%d %B, %Y %H:%M:%S')
				if datetime.strftime(i[0], '%d %B, %Y') not in self.dates and x > datetime.strftime(present.date(), '%d %B, %Y %H:%M:%S'):
					self.dates.append(datetime.strftime(
						i[0], '%d %B, %Y %I:%M %p'))

		for i in res:
			if i[0] == self.n:
				self.movdesc, self.movposter, self.movie_price, self.movie_rating, self.cast, self.runtime, self.director, self.languages, self.genre, self.rated = i[
					2], i[1], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]

		self.bookbutton = QPushButton(self.centralwidget)
		self.bookbutton.setObjectName(u"button")
		self.bookbutton.setGeometry(QRect(570, 800, 1300, 100))
		self.bookbutton.setStyleSheet(
			"QPushButton{font-size: 40pt;background-color : rgba(188, 90, 128, 1); padding:10px}")
		#self.bookbutton.clicked.connect(self.openmoviebookingscreen)

		self.open_about = False
		self.openAction = QtWidgets.QAction('About', self)
		self.bookbutton.clicked.connect(self.aboutDialog)

		self.ShowTimings = QLabel(self.centralwidget)
		self.ShowTimings.setObjectName(u"ShowTimings")
		self.ShowTimings.setGeometry(QRect(1500, 150, 800, 500))
		self.MovieInfo = QLabel(self.centralwidget)
		self.MovieInfo.setObjectName(u"Cast")
		self.MovieInfo.setGeometry(QRect(575, 280, 800, 500))
		self.MovieInfo.setStyleSheet("QLabel{font-size: 15pt;}")
		self.MovieInfo.setWordWrap(True)
		self.MovieInfo.setFont(font)

		self.movpos = QLabel(self.centralwidget)
		self.movpos.setObjectName(u"movpos")
		self.movpos.setGeometry(QRect(50, 200, 500, 700))
		self.movpos.setPixmap(
			QPixmap(self.movposter))
		self.movpos.setScaledContents(True)

		self.Title = QLabel(self.centralwidget)
		self.Title.setObjectName(u"Title")
		self.Title.setGeometry(QRect(570, 35, 40000, 400))
		self.Title.setStyleSheet("QLabel{font-size: 50pt;}")
		self.Title.setFont(font)
		self.availabel = QLabel("Available Timings", self.centralwidget)
		self.availabel.setGeometry(QRect(1550, 300, 350, 50))
		self.availabel.setStyleSheet("QLabel{font-size: 20pt;}")

		group = QButtonGroup()

		for i in range(len(self.dates)):
			mov = QPushButton(self.dates[i] if self.dates[i] else 'NO AVAILABLE SHOWTIMES', self.centralwidget)
			group.addButton(mov, i)
			mov.setObjectName(f"mov_0{i}")
			mov.setGeometry(QRect(1575, 350 + 60*i, 250, 40))

		self.bg.raise_()
		self.RedHead.raise_()
		self.label.raise_()
		self.ShowTimings.raise_()
		self.MovieInfo.raise_()
		self.bookbutton.raise_()
		self.Title.raise_()
		self.movpos.raise_()

		MovieInfoWindow.setCentralWidget(self.centralwidget)
		self.retranslateUi(MovieInfoWindow)

		QMetaObject.connectSlotsByName(MovieInfoWindow)

	def retranslateUi(self, MovieInfoWindow):
		MovieInfoWindow.setWindowTitle(QCoreApplication.translate(
			"MovieInfoWindow", u"MovieInfoWindow", None))
		self.label.setText("")
		self.RedHead.setText("")
		self.bookbutton.setText("BOOK NOW")
		self.bg.setText(QCoreApplication.translate(
			"MovieInfoWindow", u"", None))
		self.MovieInfo.setText(QCoreApplication.translate(
			"MovieInfoWindow", f"{self.movdesc}\nGenre : {self.genre}\nDirector : {self.director}\nAge Rating : {self.rated}\nRuntime : {self.runtime}\nCast : {self.cast}\nRating : {self.movie_rating}", None))
		self.movpos.setText(QCoreApplication.translate(
			"MovieInfoWindow", u"", None))
		self.Title.setText(QCoreApplication.translate(
			"MovieInfoWindow", self.n, None))

	def getmovname(self):
		n = json.load(open(r'CineDeck\vari.json'))['movname']
		return n

	def about_state_upd(self, value):
		self.open_about = value

	def aboutDialog(self):
		self.close()
		self._about = AboutDialog(self)
		self._about.exec_()


class AboutDialog(QtWidgets.QDialog):

	def __init__(self, parent):
		super(AboutDialog, self).__init__(parent)
		self.booking = Ui_MovieBookingWindow()

		self.setMinimumSize(400, 350)
		self.parent().about_state_upd(True)
		self.setWindowTitle("Verification")

		QBtn = QDialogButtonBox.Ok

		self.buttonBox = QDialogButtonBox(QBtn)
		self.buttonBox.accepted.connect(self.closeEvent)

		self.layout = QVBoxLayout()
		message = QLabel("Click OK to continue.\n(Human Verification)")
		self.layout.addWidget(message)
		self.layout.addWidget(self.buttonBox)
		self.setLayout(self.layout)

	def closeEvent(self, closeEvent=None):
		self.parent().about_state_upd(False)
		self.close()
		self.booking.show()


