from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit, QHBoxLayout, QLabel, QLineEdit, QComboBox)
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from PyQt5.QtCore import QDate, Qt

class View(QWidget):

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):
        self.lbl1 = QLabel(self.date.toString(Qt.DefaultLocaleLongDate), self)

        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)

        self.btn1 = QPushButton('Calc',self)
        self.btn2 = QPushButton('Clear',self)

        self.le1 = QLineEdit('0', self)
        self.le1.setAlignment(QtCore.Qt.AlignRight)
        self.le1.setFocus(True)
        self.le1.selectAll()

        self.le2 = QLineEdit('0', self)
        self.le2.setAlignment(QtCore.Qt.AlignRight)

        self.cb = QComboBox(self)
        self.cb.addItems(['+', '-', '*', '/', '^', '%'])

        hbox_formular = QHBoxLayout()
        hbox_formular.addWidget(self.le1)
        hbox_formular.addWidget(self.cb)
        hbox_formular.addWidget(self.le2)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        vbox = QVBoxLayout()
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox_formular)
        vbox.addLayout(hbox)
        vbox.addWidget(self.lbl1)

        self.setLayout(vbox)

        self.setWindowTitle('calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(500,500)
        self.show()
    
    def setDisplay(self, text):
        self.te1.appendPlainText(text)
    
    def clearMessage(self):
        self.te1.clear()