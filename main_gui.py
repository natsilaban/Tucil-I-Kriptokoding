import sys
import vigenere_alphabet as va
import vigenere_extended as ve
import playfair as pf
import onetimepad as otp
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QMainWindow
from PyQt6.uic import loadUi

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("uiciper.ui", self)

        self.comboBoxMethod_2.activated.connect(self.method)
        print("wek1")

    def method(self):
        if (self.comboBoxMethod_2.currentText() == "Encrypt"):
            self.comboBoxMethod.activated.connect(self.methodEncrypt)
        elif (self.comboBoxMethod_2.currentText() == "Decrypt"):
            self.comboBoxMethod.activated.connect(self.methodDecrypt)   

    def methodEncrypt(self):
        if (self.comboBoxMethod.currentText() == "Vigenere Standard"):
            print("wek2")
            self.generateButton.clicked.connect(self.vigenereEn)

        elif (self.comboBoxMethod.currentText() == "Extended Vigenere Cipher"):
            print("s")
            self.generateButton.clicked.connect(self.vigenereExEn)    

        elif (self.comboBoxMethod.currentText() == "Playfair Cipher"):
            print("s")    
            self.generateButton.clicked.connect(self.playfairEn)

        elif (self.comboBoxMethod.currentText() == "One-time Pad"):
            print("s")    

    def methodDecrypt(self):
        if (self.comboBoxMethod.currentText() == "Vigenere Standard"):
            print("wek2")
            self.generateButton.clicked.connect(self.vigenereDe)

        elif (self.comboBoxMethod.currentText() == "Extended Vigenere Cipher"):
            print("s")
            self.generateButton.clicked.connect(self.vigenereExDe)    

        elif (self.comboBoxMethod.currentText() == "Playfair Cipher"):
            print("s")    
            self.generateButton.clicked.connect(self.playfairDe)

        elif (self.comboBoxMethod.currentText() == "One-time Pad"):
            print("s")    

    def vigenereEn(self):
        key = self.textEditKey.toPlainText()
        text = self.textEditPlaintext.toPlainText()
        encrypted = va.encryptText(text, key)
        self.textHasiltanpaspace.setText(encrypted)
        encryptedSpasi = perLima(encrypted)
        self.textHasilKelompok.setText(encryptedSpasi)
        print("wek")

    def vigenereExEn(self):
        key = self.textEditKey.toPlainText()
        text = self.textEditPlaintext.toPlainText()
        text = "testpdf.pdf"
        a = ve.pathInput(text)
        encrypted = ve.encryptExt(a, key)
        print("wek")
        return ve.writeFile(a, encrypted)
        

    def playfairEn(self):
        key = self.textEditKey.toPlainText()
        text = self.textEditPlaintext.toPlainText()
        encrypted = pf.encryptPlayfair(key, text)
        self.textHasiltanpaspace.setText(encrypted)
        encryptedSpasi = perLima(encrypted)
        self.textHasilKelompok.setText(encryptedSpasi)

    def onetimepadEn(self):
        key = self.textEditKey.toPlainText()
        text = self.textEditPlaintext.toPlainText() + '.txt'
        otp.generateRandomKey(text)
        encrypted = va.encryptText(key, text)
        self.textHasiltanpaspace.setText(encrypted)
        encryptedSpasi = perLima(encrypted)
        self.textHasilKelompok.setText(encryptedSpasi)        

    def vigenereDe(self):
        key = self.textEditKey.toPlainText()
        text = self.textEditPlaintext.toPlainText()
        decrypted = va.decryptText(text, key)
        self.textHasiltanpaspace.setText(decrypted)
        decryptedSpasi = perLima(decrypted)
        self.textHasilKelompok.setText(decryptedSpasi)
        print("wek")

    def vigenereExDe(self):
        key = self.textEditKey.toPlainText()
        text = self.textEditPlaintext.toPlainText()
        encrypted = ve.decryptExt(text, key)
        self.textHasiltanpaspace.setText(encrypted)
        encryptedSpasi = perLima(encrypted)
        self.textHasilKelompok.setText(encryptedSpasi)
        print("wek")    

    def playfairDe(self):
        key = self.textEditKey.toPlainText()
        text = self.textEditPlaintext.toPlainText()
        decrypted = pf.encryptPlayfair(key, text)
        self.textHasiltanpaspace.setText(decrypted)
        decryptedSpasi = perLima(decrypted)
        self.textHasilKelompok.setText(decryptedSpasi)


def perLima(text):
    perLima = ""
    group = 0
    for i in range(5, len(text), 5):
        if group != 0:
            perLima = perLima + " " + (text[group:i])
        else:
            perLima = text[group:i]
        group = i
    perLima = perLima + " " + (text[group:])
    return perLima
        


app = QApplication(sys.argv)
window = Window()
window.show()
window.setWindowTitle("Tucil Chiper")
sys.exit(app.exec())