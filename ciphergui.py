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
        # self.cb.currentIndexChanged.connect(self.selectionchange)
        
        self.generalLayout.addWidget(self.cb)

        self.form = QFormLayout()
        self.key = QLineEdit()
        self.text = QLineEdit()
        self.form.addRow("Key:", self.key)
        self.form.addRow("Text:", self.text)

        self.generalLayout.addLayout(self.form)

        runBtn = QPushButton("Ok")

        self.generalLayout.addWidget(runBtn)

        # if (self.cb.currentText() == "Vigenere"):
        #     runBtn.clicked.connect(vigenere(self.key.text(), self.text.text()))

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
   
def vigenere(key, text):
    return (va.encryptText(text, key))

# class VigenereCipher:
#     def __init__(self, model, view):
#         self._evaluate = model
#         self._view = view
#         self._connectSignalsAndSlots()

#     def _calculateResult(self):
#         result = self._evaluate(expression=self._view.displayText())
#         self._view.setDisplayText(result)

#     def _buildExpression(self, subExpression):
#         if self._view.displayText() == ERROR_MSG:
#             self._view.clearDisplay()
#         expression = self._view.displayText() + subExpression
#         self._view.setDisplayText(expression)

#     def _connectSignalsAndSlots(self):
#         for keySymbol, button in self._view.buttonMap.items():
#             if keySymbol not in {"=", "C"}:
#                 button.clicked.connect(
#                     partial(self._buildExpression, keySymbol)
#                 )
#         self._view.buttonMap["="].clicked.connect(self._calculateResult)
#         self._view.display.returnPressed.connect(self._calculateResult)
#         self._view.buttonMap["C"].clicked.connect(self._view.clearDisplay)


def main():
    app = QApplication([])
    cipherWindow = CipherWindow()
    cipherWindow.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
