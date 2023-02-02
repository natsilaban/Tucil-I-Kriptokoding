import vigenere_alphabet as va
import sys
from functools import partial

from PyQt6.QtWidgets import (
    QApplication,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLabel,
    QComboBox,
    QFormLayout,
    QDialog,
    QDialogButtonBox
)

ERROR_MSG = "ERROR"
WINDOW_SIZE = 500
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40


class CipherWindow(QDialog):
    """PyCalc's main window (GUI or view)."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cipher")
        
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        #self.setCentralWidget(centralWidget)
        self.generalLayout.addWidget(QLabel("<h1>Welcome to Tugas 1 Kriptografi & Koding</h1>", parent=centralWidget))
        self.generalLayout.addWidget(QLabel("Masukkan pilihan cipher!", parent=centralWidget))

        self.cb = QComboBox()
        self.cb.addItem("Vigenere")
        self.cb.addItem("Extended Vigenere")
        self.cb.addItem("Playfair")
        self.cb.addItem("One-Time Pad")
        self.cb.currentIndexChanged.connect(self.selectionchange)
        
        self.generalLayout.addWidget(self.cb)

        self.form = QFormLayout()
        self.key = QLineEdit()
        self.text = QLineEdit()
        self.form.addRow("Key:", self.key)
        self.form.addRow("Text:", self.text)

        self.generalLayout.addLayout(self.form)

        runBtn = QPushButton("Ok")

        self.generalLayout.addWidget(runBtn)

        if (self.cb.currentText() == "Vigenere"):
            runBtn.clicked.connect(self.vigenere(self.key.text(), self.text.text()))

        # button cipher choice
        # vigenereBtn = QPushButton("Vigenere")
        # vigenereExtendedBtn = QPushButton("Extended Vigenere")
        # playfairBtn = QPushButton("Playfair")
        # otpBtn = QPushButton("One-Time Pad")

        # vigenereBtn.clicked.connect(self.chooseCipher)
        # vigenereExtendedBtn.clicked.connect(self.chooseCipher)
        # playfairBtn.clicked.connect(self.chooseCipher)
        # otpBtn.clicked.connect(self.chooseCipher)

        # self.generalLayout.addWidget(vigenereBtn)
        # self.generalLayout.addWidget(vigenereExtendedBtn)
        # self.generalLayout.addWidget(playfairBtn)
        # self.generalLayout.addWidget(otpBtn)
        centralWidget.setLayout(self.generalLayout)

    # def chooseCipher(self):
    #     self.generalLayout.addWidget(QLineEdit(self))

    def selectionchange(self):
        cipherChoice = self.cb.currentText()
        return cipherChoice

    def vigenere(self, key, text):
        print(va.encryptText(key, text))
        
            
class VigenereCipher(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vigenere")
        QLabel("ngok")

def main():
    app = QApplication([])
    cipherWindow = CipherWindow()
    cipherWindow.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
