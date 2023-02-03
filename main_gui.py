import sys
from vigenere_alphabet import *
from vigenere_extended import *
from PyQt6 import QtCore, QtGui, QtWidgets, QMainQindow, QApplication
from PyQt6.uic import loadUi

class Menu(QMainQindow):
    def __init__(self):
        super(Menu, self).__init__()
        loadUi("uiciper.ui", self)
        self.combo_box.current

    current = self.comboBoxMethod.curentText()

    if (current == "Vigenere Standard"):
        self.label.setText("Content : " + current)

    elif (current == "Extended Vigenere Cipher"):
        self.label.setText("Content : " + current)

    elif (current == "Playfair Cipher"):
        self.label.setText("Content : " + current)

    elif (current == "One-time Pad"):
        self.label.setText("Content : " + current)                

app = QApplication(sys.argv)
welcome = Menu()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Bye - bye")