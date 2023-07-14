from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import mysql.connector as mc
from datetime import *
import json
from ui_payment import *
mydb = mc.connect(
	host="localhost",
	user="root",
	password='Amongoose_123',
	database="cinedeck")
listofseats = []
cur = mydb.cursor()

class Ui_SeatsWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()

	def setupUi(self, SeatsWindow):
		if not SeatsWindow.objectName():
			SeatsWindow.setObjectName(u"SeatsWindow")
		self.movnameee = self.getmovname()
		self.showe = self.getshow()

		cur.execute(
			f"select halls from halls where movie_name = '{self.movnameee}' and showtimings = '{datetime.strptime(self.showe, '%Y-%m-%d %H:%M:%S')}'")
		self.hall = cur.fetchall()[0][0]

		font = QFont()
		font.setFamily(u"Yu Gothic UI Light")
		font.setPointSize(9)
		self.centralwidget = QtWidgets.QWidget(SeatsWindow)
		self.centralwidget.setObjectName(u"centralwidget")
		self.label = QLabel(self.centralwidget)
		self.label.setObjectName(u"label")
		self.label.setGeometry(QRect(770, -30, 870, 200))
		self.label.setPixmap(QPixmap(r"CineDeck\assets\logo.svg"))
		self.RedHead = QLabel(self.centralwidget)
		self.RedHead.setObjectName(u"RedHead")
		self.RedHead.setGeometry(QRect(0, -20, 1920, 150))
		self.RedHead.setStyleSheet(u"background-color: rgba(128, 0, 0, 1)")
		self.label.raise_()
		exen = QLabel("           Entrance/Exit", self.centralwidget)
		exen.setGeometry(QRect(1600, 850, 200, 30))

		exen.setStyleSheet(u"background-color: rgba(128, 0, 0, 0.6)")
		exen1 = QLabel("           Entrance/Exit", self.centralwidget)
		exen1.setGeometry(QRect(50, 250, 30, 200))
		self.book = QPushButton("BOOK SEATS!", self.centralwidget)
		self.book.setGeometry(QRect(1700, 150, 200, 40))
		self.book.clicked.connect(self.aboutDialog)
		exen1.setStyleSheet(u"background-color: rgba(128, 0, 0, 0.6)")
		self.screen = QLabel(self.centralwidget)
		self.screen.setText(
			"                                                                            SCREEN")
		self.screen.setStyleSheet(
			u"QLabel{background-color: rgba(128, 0, 0, 0.2) ;}")
		self.screen.setGeometry(QRect(540, 200, 800, 40))
		#region regular
		self.regseats = QButtonGroup()
		self.regseats.setExclusive(False)
		for i in range(1, 91):
			cur.execute(
				f"select reg from halls where (movie_name = '{self.movnameee}' and showtimings = '{datetime.strptime(self.showe, '%Y-%m-%d %H:%M:%S')}' and halls = {self.hall})")
			y = cur.fetchall()
			self.seat = QPushButton(self.centralwidget, checkable=True)
			self.seat.setObjectName(f"{i}R")
			if y != [(None,)]:
				if f" {i}R" in (y[0][0]):
					self.seat.setDisabled(True)
					self.seat.setStyleSheet(
						"QPushButton{background-color: rgba(108, 122, 137, 0.6)}")
				else:
					self.seat.setStyleSheet(
						"QPushButton{background-color: rgba(18, 122, 17, 0.6)}QPushButton:checked{background-color: rgba(132, 82, 1, 0.6)}")
			else:
				self.seat.setStyleSheet(
					"QPushButton{background-color: rgba(18, 122, 17, 0.6)}QPushButton:checked{background-color: rgba(132, 82, 1, 0.6)}")
			self.regseats.addButton(self.seat)
			if i <= 30:
				labelm = QLabel(f'A-{i}R', self.centralwidget)
				labelm.setGeometry(QRect(60 + 57 * i, 300, 55, 55))

				self.seat.setGeometry(QRect(60 + 57 * i, 300, 55, 55))
			elif 30 < i <= 60:
				labelm = QLabel(f'B-{i-30}R', self.centralwidget)
				labelm.setGeometry(QRect(60 + 57 * (i-30), 375, 55, 55))
				self.seat.setGeometry(QRect(60 + 57 * (i-30), 375, 55, 55))
			elif 60 < i <= 91:
				labelm = QLabel(f'C-{i-60}R', self.centralwidget)
				labelm.setGeometry(QRect(60 + 57 * (i-60), 450, 55, 55))
				self.seat.setGeometry(QRect(60 + 57 * (i-60), 450, 55, 55))
			self.seat.raise_()
			self.seat.clicked.connect(self.addseats)
		#endregion

		#region vip
		self.vipseats = QButtonGroup()
		self.vipseats.setExclusive(False)
		for i in range(1, 41):
			cur.execute(
				f"select vip from halls where (movie_name = '{self.movnameee}' and showtimings = '{datetime.strptime(self.showe, '%Y-%m-%d %H:%M:%S')}' and halls = {self.hall})")
			y = cur.fetchall()
			self.vseat = QPushButton(self.centralwidget, checkable=True)
			self.vseat.setObjectName(f"{i}V")
			if y != [(None,)]:
				if f" {i}V" in (y[0][0]):
					self.vseat.setDisabled(True)
					self.vseat.setStyleSheet(
						"QPushButton{background-color: rgba(108, 122, 137, 0.6)}")
				else:
					self.vseat.setStyleSheet(
						"QPushButton{background-color: rgba(238, 15, 227, .6)}QPushButton:checked{background-color: rgba(132, 82, 1, 0.6)}")
			else:
				self.vseat.setStyleSheet(
					"QPushButton{background-color: rgba(238, 15, 227, .6)}QPushButton:checked{background-color: rgba(132, 82, 1, 0.6)}")

			self.vipseats.addButton(self.vseat)
			if i <= 20:
				labelm = QLabel(f'V-A-{i}', self.centralwidget)
				labelm.setGeometry(QRect(240 + 70 * i, 550, 55, 55))
				self.vseat.setGeometry(QRect(240 + 70 * i, 550, 55, 55))
			elif 20 < i <= 41:
				labelm = QLabel(f'V-B-{i-20}', self.centralwidget)
				labelm.setGeometry(QRect(240 + 70 * (i-20), 625, 55, 55))
				self.vseat.setGeometry(QRect(240 + 70 * (i-20), 625, 55, 55))
			self.vseat.raise_()
			self.vseat.clicked.connect(self.addseats)

		#endregion

		#region vipb
		self.vipbseats = QButtonGroup()
		self.vipbseats.setExclusive(False)
		for i in range(1, 21):
			cur.execute(
				f"select vipb from halls where (halls = {self.hall} and movie_name = '{self.movnameee}' and showtimings = '{datetime.strptime(self.showe, '%Y-%m-%d %H:%M:%S')}')")
			y = cur.fetchall()
			self.seatb = QPushButton(self.centralwidget, checkable=True)
			self.seatb.setObjectName(f"{i}B")
			self.vipbseats.addButton(self.seatb)
			if y != [(None,)]:
				if f" {i}B" in (y[0][0]):
					self.seatb.setDisabled(True)
					self.seatb.setStyleSheet(
						"QPushButton{background-color: rgba(108, 122, 137, 0.6)}")
				else:
					self.seatb.setStyleSheet(
						"QPushButton{background-color:  rgba(18, 12, 137, 0.6)}QPushButton:checked{background-color: rgba(132, 82, 1, 0.6)}")
			else:
				self.seatb.setStyleSheet(
                                    "QPushButton{background-color: rgba(18, 12, 137, 0.6)}QPushButton:checked{background-color: rgba(132, 82, 1, 0.6)}")
			if i <= 10:
				labelm = QLabel(f'VB-A-{i}', self.centralwidget)
				labelm.setGeometry(QRect(100 + 70 * i, 725, 55, 55))
				self.seatb.setGeometry(QRect(100 + 70 * i, 725, 55, 55))
			elif 10 < i <= 21:
				labelm = QLabel(f'VB-B-{i-10}', self.centralwidget)
				labelm.setGeometry(QRect(100 + 70 * (i-10), 800, 55, 55))
				self.seatb.setGeometry(QRect(100 + 70 * (i-10), 800, 55, 55))
			self.seatb.raise_()
			self.seatb.clicked.connect(self.addseats)
		#endregion

		#region prem
		self.prem = QButtonGroup()
		self.prem.setExclusive(False)
		for i in range(1, 11):
			cur.execute(
				f"select prem from halls where (halls = {self.hall} and movie_name = '{self.movnameee}' and showtimings = '{datetime.strptime(self.showe, '%Y-%m-%d %H:%M:%S')}')")
			y = cur.fetchall()
			self.pseat = QPushButton(self.centralwidget, checkable=True)
			self.pseat.setObjectName(f"{i}P")
			if y != [(None,)]:
				if f" {i}P" in (y[0][0]):
					self.pseat.setDisabled(True)
					self.pseat.setStyleSheet(
						"QPushButton{background-color: rgba(108, 122, 137, 0.6)}")
				else:
					self.pseat.setStyleSheet("QPushButton{background-color:rgba(13, 84, 127, 0.6)}QPushButton:checked{background-color: rgba(132, 82, 1, 0.6)}")
			else:
				self.pseat.setStyleSheet("QPushButton{background-color: rgba(13, 84, 127, 0.6)}QPushButton:checked{background-color: rgba(132, 82, 1, 0.6)}")

			self.prem.addButton(self.pseat)
			if i <= 5:
				labelm = QLabel(f'VP-A-{i}', self.centralwidget)
				labelm.setGeometry(QRect(1000 + 70 * i, 725, 55, 55))
				self.pseat.setGeometry(QRect(1000 + 70 * i, 725, 55, 55))
			elif 5 < i <= 11:
				labelm = QLabel(f'VP-B-{i-5}', self.centralwidget)
				labelm.setGeometry(QRect(1000 + 70 * (i-5), 800, 55, 55))
				self.pseat.setGeometry(QRect(1000 + 70 * (i-5), 800, 55, 55))
			self.pseat.raise_()
			self.pseat.clicked.connect(self.addseats)
		#endregion

		SeatsWindow.setCentralWidget(self.centralwidget)
		QMetaObject.connectSlotsByName(SeatsWindow)
		exen.raise_()

	def addseats(self):
		sentbutton = self.sender()
		if self.sender().isChecked():
			listofseats.append(sentbutton.objectName())
			print(listofseats)
		else:
			listofseats.remove(sentbutton.objectName())
			print(listofseats)


	def getmovname(self):
		n = json.load(open(r'CineDeck\vari.json'))['movname']
		return n

	def getshow(self):
		f = open(r'CineDeck\show.txt')
		s = f.readline()
		return s

	def about_state_upd(self, value):
		self.open_about = value

	def aboutDialog(self):
		self.close()
		self._about = AboutDialog(self)
		self._about.exec_()

class AboutDialog(QtWidgets.QDialog):

	def __init__(self, parent):
		super(AboutDialog, self).__init__(parent)
		self.payment = Ui_PaymentWindow()
		self.setMinimumSize(400, 350)
		self.parent().about_state_upd(True)
		self.setWindowTitle("Prices")

		QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
		self.movnameee = self.getmovname()
		self.showe = self.getshow()
		cur.execute(
                    f"select halls from halls where movie_name = '{self.movnameee}' and showtimings = '{datetime.strptime(self.showe, '%Y-%m-%d %H:%M:%S')}'")
		self.hall = cur.fetchall()[0][0]

		self.buttonBox = QDialogButtonBox(QBtn)
		self.buttonBox.accepted.connect(self.bookseats)
		self.buttonBox.rejected.connect(self.closeEvent)
		cur.execute(f"select price, pricevip, pricevipb, priceprem from shows where movie_name = '{self.movnameee}' and hall = {self.hall} and showtimings = '{self.showe}'")
		cost = cur.fetchall()[0]
		reg, v, vb, prem = [], [], [], []
		for i in listofseats:

			if i[-1] == 'R':
				reg.append(i)
			if i[-1] == 'V':
				v.append(i)
			if i[-1] == 'B':
				vb.append(i)
			if i[-1] == 'P':
				prem.append(i)
		total = cost[0] * len(reg) + cost[1] * len(v) + cost[2] * len(vb) + cost[3] * len(prem)
		message1 = QLabel(
			f"Regular --> {cost[0]} x {len(reg)}  =  {cost[0] * len(reg)}\nVIP --> {cost[1]} x {len(v)}  =  {cost[1] * len(v)}\nVIP Blue --> {cost[2]} x {len(vb)}  =  {cost[2] * len(vb)}\nPremium --> {cost[3]} x {len(prem)}  =  {cost[3] * len(prem)}\n--------------------------------\nTotal : {total} AED")
		self.layout = QVBoxLayout()
		self.layout.addWidget(message1)
		self.layout.addWidget(self.buttonBox)
		self.setLayout(self.layout)

	def closeEvent(self, closeEvent=None):
		self.parent().about_state_upd(False)
		self.close()

	def bookseats(self):
		import pickle
		self.close()
		self.payment.show()
		with open('seats.dat', 'wb') as fh:
			pickle.dump(listofseats, fh)

	def getmovname(self):
		n = json.load(open(r'CineDeck\vari.json'))['movname']
		return n

	def getshow(self):
		f = open(r'CineDeck\show.txt')
		s = f.readline()
		return s

