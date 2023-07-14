
from datetime import timedelta
from datetime import datetime
from datetimerange import DateTimeRange
import datetime
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys, PySide2

import mysql.connector as mc

from PySide2.QtSql import *
from PySide2.QtGui import *

from datetime import datetime, timedelta
from ui_seats import *


mydb = mc.connect(
	host="localhost",
	user="root",
	password='Amongoose_123',
	database="cinedeck")
cur = mydb.cursor(buffered=True)

cur.execute(f"select movie_name, showtimings, showend from shows")
resss = cur.fetchall()


class Ui_UpdateShowTimingsScreen(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.seats = Ui_SeatsWindow()

	def addmovie(self):

		movname = self.movname.text()

		cur.execute(f"SELECT movie_name, runtime from movies where movie_name = '{movname}'")
		res = cur.fetchall()


		showtimings = f"{self.DateTime.text().replace('/', '-')}"
		hall = int(self.HallNumber.text())
		price = int(self.price.text())
		pricevip = int(self.pricevip.text())
		pricevipb = int(self.pricevipb.text())
		priceprem = int(self.priceprem.text())

		if res:
			time = datetime.strptime(showtimings, '%Y-%m-%d %H:%M:%S')
			endtime = time + timedelta(minutes=int(res[0][1].split()[0]))
			cur.execute(
                            f"SELECT showtimings, showend FROM SHOWS where hall = {hall}")
			xe = cur.fetchall()
			flag = True
			for i in xe:
				starttime = i[0]
				endttime = i[1]
				time_range = DateTimeRange(starttime, endttime)
				flag = True if (time not in time_range and endtime not in time_range) else False
			if flag:
				cur.execute((f"INSERT INTO shows(movie_name, showtimings, showend, hall, price, pricevip, pricevipb, priceprem) VALUES('{movname}', '{showtimings}', '{endtime}', {hall}, {price}, {pricevip}, {pricevipb}, {priceprem})"))
				cur.execute(
					f"INSERT INTO halls(movie_name, halls, showtimings, showend) VALUES('{movname}', {hall}, '{showtimings}', '{endtime}')")
				mydb.commit()
				with open(r'CineDeck\show.txt', 'w') as fh:
					fh.write(str(showtimings))
					fh.flush()
				with open(r'CineDeck\hall.txt', 'w') as f:
					f.write(str(hall))
					f.flush()
			else:
				QtWidgets.QMessageBox.about(self, "Error", "Hall already booked for this timeslot.")


		else:
			QtWidgets.QMessageBox.critical(self, "Error", "Incorrect Details!")

	def setupUi(self, ShowTimings):
		if not ShowTimings.objectName():
			ShowTimings.setObjectName(u"ShowTimings")
		ShowTimings.resize(1920, 1080)
		self.centralwidget = QtWidgets.QWidget(ShowTimings)
		self.centralwidget.setObjectName(u"centralwidget")
		ShowTimings.setCentralWidget(self.centralwidget)
		self.label = QLabel(self.centralwidget)
		self.label.setObjectName(u"label")
		self.label.setGeometry(QRect(770, -30, 870, 200))
		self.label.setPixmap(QPixmap(r"CineDeck\assets\logo.svg"))
		self.RedHead = QLabel(self.centralwidget)
		self.RedHead.setObjectName(u"RedHead")
		self.RedHead.setGeometry(QRect(0, -20, 1920, 150))
		self.projectModel = QSqlQueryModel()

		# self.projectView = QTableView()
		# self.projectView.setModel(res1)
		self.RedHead.setStyleSheet(u"background-color: rgba(128, 0, 0, 1)")
		self.searchmovb = QPushButton("Go", self.centralwidget)
		self.searchmovb.setObjectName(u"searchmovb")
		self.searchmovb.setGeometry(QRect(50, 725, 50, 50))
		self.searchmovb.clicked.connect(self.addmovie)
		self.searchmovb.setStyleSheet("QPushButton{font-size: 15pt;}")
		self.movname = QLineEdit(self.centralwidget)
		self.movname.setGeometry(QRect(50, 200, 400, 50))
		self.movname.setPlaceholderText("Enter Movie Name: ")
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
		cur.execute("show columns from shows")
		xxxx = cur.fetchall()
		cur.execute("Select * from shows")
		ressss = cur.fetchall()
		listt = [str(i[0]) for i in xxxx]
		self.table = QTableWidget(self.centralwidget)
		self.table.setRowCount(len(resss))
		self.table.setColumnCount(len(xxxx))
		self.table.setHorizontalHeaderLabels(listt)
		self.table.setGeometry(QRect(500, 250, 1400, 500))
		self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
		for row_number, row_data in enumerate(ressss):
			for column_number, data in enumerate(row_data):
				self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

		self.RedHead.raise_()
		self.label.raise_()
		# self.hall.raise_()
		# self.dates.raise_()
		self.movname.raise_()
		# self.searchmovb.raise_()

		self.retranslateUi(ShowTimings)

		QMetaObject.connectSlotsByName(ShowTimings)

	def retranslateUi(self, ShowTimings):
		ShowTimings.setWindowTitle(QCoreApplication.translate(
			"ShowTimings", u"ShowTimings", None))
		self.label.setText("")
		self.RedHead.setText("")

	def openseats(self):
		self.seats.setupUi(self)

