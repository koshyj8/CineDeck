from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import mysql.connector as mc
from datetime import *
import json
import PySide2
import sys
import re

nn = json.load(open(r'CineDeck\vari.json'))['movname']

mydb = mc.connect(
	host="localhost",
	user="root",
	password='Amongoose_123',
	database="cinedeck")

cur = mydb.cursor()


class Ui_PaymentWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

	def setupUi(self, PaymentWindow):
		font = QFont()
		font.setFamily(u"Yu Gothic UI")
		font.setPointSize(9)
		PaymentWindow.setObjectName(u"PaymentWindow")
		PaymentWindow.resize(1920, 1080)

		cur.execute(f"select movie_poster from movies where movie_name = '{nn}'")
		dire = cur.fetchall()[0][0]


		self.centralwidget = QtWidgets.QWidget(PaymentWindow)
		self.centralwidget.setObjectName(u"centralwidget")
		self.label = QLabel(self.centralwidget)
		self.label.setObjectName(u"label")
		self.label.setGeometry(QRect(770, -30, 870, 200))
		self.label.setPixmap(QPixmap(r"CineDeck\assets\logo.svg"))
		"""self.movpos = QLabel(self.centralwidget)
		self.movpos.setObjectName(u"movpos")
		self.movpos.setGeometry(QRect(900, 200, 500, 700))
		self.movpos.setPixmap(
			QPixmap(dire))"""
		self.RedHead = QLabel(self.centralwidget)
		self.RedHead.setObjectName(u"RedHead")
		self.RedHead.setGeometry(QRect(0, -20, 1920, 150))
		self.RedHead.setStyleSheet(u"background-color: rgba(128, 0, 0, 1)")

		self.cardnumber = QLineEdit(self.centralwidget)
		self.cardnumber.setMaxLength(16)
		self.cardnumber.setPlaceholderText("1234 5678 0000")
		self.cardnumber.setInputMask(("dddd "*4)[:-1])
		self.cardnumber.setGeometry(QRect(50, 200, 500, 40))
		self.cardnumberlabel = QLabel("Card Number: ", self.centralwidget)
		self.cardnumberlabel.setFont(font)
		self.cardnumberlabel.setGeometry(QRect(50, 165, 500, 40))

		self.doe = QDateEdit(self.centralwidget)
		self.doe.setGeometry(QRect(50, 270, 500, 40))
		self.doelabel = QLabel("Expiration Date: ", self.centralwidget)
		self.doelabel.setFont(font)
		self.doelabel.setGeometry(QRect(50, 235, 500, 40))
		self.doe.setMinimumDate(QDate.currentDate())

		self.cvv = QLineEdit(self.centralwidget)
		self.cvv.setMaxLength(4)
		self.cvv.setGeometry(QRect(50, 340, 500, 40))
		self.cvvlabel = QLabel("CVV: ", self.centralwidget)
		self.cvvlabel.setFont(font)
		self.cvvlabel.setGeometry(QRect(50, 305, 500, 40))

		self.pay = QPushButton(self.centralwidget)
		self.pay.clicked.connect(self.payprice)
		self.pay.setGeometry(QRect(50, 390, 100, 40))
		self.pay.setText("Pay Now!")

		PaymentWindow.setCentralWidget(self.centralwidget)

		self.label.raise_()

		QMetaObject.connectSlotsByName(PaymentWindow)


	def payprice(self):
		import pickle
		cardnum = self.cardnumber.text()
		date = self.doe.text()
		cvv = self.cvv.text()



		with open(r'CineDeck\username.txt', 'r') as f:
			x = f.readline()
			print(x)


		n = json.load(open(r'CineDeck\vari.json'))['movname']
		showe = self.getshow()
		cur.execute(
			f"select halls from halls where movie_name = '{n}' and showtimings = '{datetime.strptime(showe, '%Y-%m-%d %H:%M:%S')}'")
		self.hall = cur.fetchall()[0][0]
		with open(r'CineDeck\show.txt', 'r') as f:
			datee = f.readline()
			date = date[0:10]
		tid = str(n) + str(datee)
		cur.execute(f"select * from tickets where id = '{tid}'")
		if not cur.fetchall():
			cur.execute(f"insert into tickets(id, showtime) values('{tid}', '{datee}')")
		cur.execute(f"update user_info set ticket = '{tid}' where email = '{x}'")
		mydb.commit()
		with open('seats.dat', 'rb') as fh:
			listofseats = pickle.load(fh)

		QMessageBox.information(
                    self, "Success", f"Successfully booked show for {n} on:\n{datetime.strftime(datetime.strptime(datee, '%Y-%m-%d %H:%M:%S'),  '%d %B, %Y %H:%M:%S')}")
		if len(listofseats) == 0:
			QtWidgets.QMessageBox.critical(self, "Error", "Please select atleast one seat!")
		for i in listofseats:
			last = i[-1]
			if last == 'R':
				seat = 'reg'
			if last == 'P':
				seat = 'prem'
			if last == 'B':
				seat = 'vipb'
			if last == 'V':
				seat = 'vip'
			cur.execute(
				f"select {seat} from halls where showtimings = '{datetime.strptime(showe, '%Y-%m-%d %H:%M:%S')}' and halls = {self.hall}")
			x = cur.fetchall()
			val = ('' if x[0][0] == None else x[0][0]) + f" {i}"
			cur.execute(
				f"UPDATE halls set {seat} = '{val}' where showtimings = '{showe}' and halls = {self.hall}")
			mydb.commit()
		sys.exit()

	def getshow(self):
		f = open(r'CineDeck\show.txt')
		s = f.readline()
		return s

