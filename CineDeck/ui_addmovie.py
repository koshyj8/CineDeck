from datetime import timedelta
from datetime import datetime
from datetimerange import DateTimeRange
import PySide2
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import requests
import mysql.connector as mc
import sys
mydb = mc.connect(
	host="localhost",
	user="root",
	password='Amongoose_123',
	database="cinedeck")


class Ui_AddMovieWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

	def addmovie(self):
		moviename1 = self.moviename.text()
		url = f'http://www.omdbapi.com/?apikey=ef7593c3&t={moviename1}&plot=full&y=2022'
		resp = requests.get(url=url)
		data = resp.json()
		cur = mydb.cursor()
		cur.execute(f"SELECT * from movies where movie_name = '{moviename1}'")
		x = cur.fetchall()
		if not x:
			if data['Response'] == 'True' and data['Runtime'] != 'N/A':
				res = data['Poster']
				response = requests.get(res)
				if response.status_code:
					fp = open(fr"CineDeck\\assets\\{data['Title']}.jpg", 'wb')
					fp.write(response.content)

				l = len(x)
				movtitle = fr"{data['Title']}".replace("\'", "\\'")
				movplot = fr"{data['Plot']}".replace("\'", "\\'")

				showtimings = f"{self.DateTime.text().replace('/', '-')}"
				hall = self.HallNumber.text()
				price = self.price.text()

				pricevip = self.pricevip.text()
				pricevipb = self.pricevipb.text()
				priceprem = self.priceprem.text()
				time = datetime.strptime(showtimings, '%Y-%m-%d %H:%M:%S')
				endtime = time + timedelta(minutes=int(data['Runtime'].split()[0]))
				cur.execute(f"SELECT showtimings, showend, hall FROM SHOWS where hall = {hall}")

				xe = cur.fetchall()
				flag = True
				for i in xe:
					starttime = i[0]
					endttime = i[1]
					time_range = DateTimeRange(starttime, endttime)
					flag = True if (
						time not in time_range and endtime not in time_range) else False
				if flag:
					if all(v is not None for v in [moviename1, hall, price, pricevip, pricevipb, priceprem]):
						hall = int(self.HallNumber.text())
						price = int(self.price.text())
						pricevip = int(self.pricevip.text())
						pricevipb = int(self.pricevipb.text())
						priceprem = int(self.priceprem.text())
						cast = data['Actors'].replace("\'", "\\'")
						query = fr"INSERT INTO movies(movie_name, movie_desc, movie_poster, movie_rating, cast, runtime, director, genre, languages, rated) VALUES('{movtitle}', '{movplot[0:254]+'...' if len(movplot) > 256 else movplot}', 'CineDeck\\assets\\{data['Title']}.jpg', '{data['Ratings'][0]['Value'] if data['Ratings'] != [] else 'None'}', '{cast}', '{data['Runtime']}', '{data['Director']}', '{data['Genre']}', '{data['Language']}', '{data['Rated']}')"
						cur.execute(query)
						cur.execute(
							(f"INSERT INTO SHOWS(movie_name, showtimings, showend, hall, price, pricevip, pricevipb, priceprem) VALUES('{movtitle}', '{showtimings}', '{endtime}', {hall}, {price}, {pricevip}, {pricevipb}, {priceprem})"))
						cur.execute(
							f"INSERT INTO halls(movie_name, halls, showtimings, showend) VALUES('{movtitle}', {hall}, '{showtimings}', '{endtime}')")
						mydb.commit()
					else:
						QtWidgets.QMessageBox.critical(self, "Error", "Enter all details!")
				else:
					QtWidgets.QMessageBox.critical(self, "Error", "Slot already taken!")

			else:
				QtWidgets.QMessageBox.critical(
					self, "Error", "Movie not available for screening.")
		else:
			QtWidgets.QMessageBox.critical(
				self, "Error", "Movie already added.")

	def setupUi(self, AddMovieWindow):
		AddMovieWindow.resize(1920, 1080)
		self.centralwidget = QtWidgets.QWidget(AddMovieWindow)
		self.centralwidget.setObjectName(u"centralwidget")
		self.label = QLabel(self.centralwidget)
		self.label.setObjectName(u"label")
		self.label.setGeometry(QRect(770, -30, 870, 200))
		self.label.setPixmap(QPixmap(r"CineDeck\assets\logo.svg"))
		self.label_2 = QLabel(self.centralwidget)
		self.label_2.setObjectName(u"label_2")
		self.label_2.setGeometry(QRect(0, -20, 1920, 150))
		self.label_2.setStyleSheet(u"background-color: rgba(128, 0, 0, 1)")
		self.moviename = QLineEdit(self.centralwidget)
		self.moviename.setGeometry(QRect(650, 500, 600, 60))
		self.moviename.setStyleSheet("QLineEdit{font-size: 25pt;}")
		self.moviename.setPlaceholderText(
			QCoreApplication.translate("AddMovieWindow", u"Enter Movie Name", None))
		self.HallNumber = QLineEdit(self.centralwidget)
		self.HallNumber.setGeometry(QRect(50, 275, 400, 50))
		self.HallNumber.setPlaceholderText("Enter Hall Number: ")
		self.price = QLineEdit(self.centralwidget)
		self.price.setGeometry(QRect(50, 425, 400, 50))
		self.price.setPlaceholderText("Enter Price for Regular Seats: ")
		self.pricevip = QLineEdit(self.centralwidget)
		self.pricevip.setGeometry(QRect(50, 500, 400, 50))
		self.pricevip.setPlaceholderText("Enter Price for VIP Seats: ")
		self.pricevipb = QLineEdit(self.centralwidget)
		self.pricevipb.setGeometry(QRect(50, 575, 400, 50))
		self.pricevipb.setPlaceholderText("Enter Price for VIP Blue Seats: ")
		self.priceprem = QLineEdit(self.centralwidget)
		self.priceprem.setGeometry(QRect(50, 650, 400, 50))
		self.priceprem.setPlaceholderText("Enter Price for Premium Seats: ")
		self.DateTime = QDateTimeEdit(self.centralwidget)
		self.DateTime.setGeometry(QRect(50, 350, 400, 50))
		self.DateTime.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
		self.DateTime.setMinimumDate(QDate.currentDate())
		self.DateTime.setMaximumDate(QDate.currentDate().addDays(50))
		self.DateTime.setMinimumTime(QTime.currentTime())
		self.DateTime.setCalendarPopup(True)
		self.button = QPushButton(self.centralwidget)
		self.button.setGeometry(QRect(650, 600, 600, 60))
		self.button.setStyleSheet("QPushButton{font-size: 20pt;}")

		self.button.clicked.connect(self.addmovie)

		"""self.label_3 = QLabel(self.centralwidget)
		self.label_3.setObjectName(u"label_2")
		self.label_3.setGeometry(QRect(270, 290, 261, 23))
		self.label_3.setStyleSheet(u"background-color: rgba(128, 0, 0, 1)")"""

		AddMovieWindow.setCentralWidget(self.centralwidget)
		self.label_2.raise_()
		self.label.raise_()
		self.moviename.raise_()

		self.retranslateUi(AddMovieWindow)

		QMetaObject.connectSlotsByName(AddMovieWindow)


	def retranslateUi(self, AddMovieWindow):
		AddMovieWindow.setWindowTitle(QCoreApplication.translate(
			"AddMovieWindow", u"AddMovieWindow", None))
		self.label.setText("")
		self.label_2.setText("")
		self.moviename.setText("")
		self.button.setText("Add Movie")


if __name__ == "__main__":
    app = PySide2.QtWidgets.QApplication(['bro im doneeee'])
    pixmap = QPixmap(r"CineDeck\assets\logo.svg")
    splash = QSplashScreen(pixmap)
    # splash.show()
    # time.sleep(5)
    ex = Ui_AddMovieWindow()
    ex.show()
    sys.exit(app.exec_())
