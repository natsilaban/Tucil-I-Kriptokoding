from PyQt6.QtWidgets import (
    QApplication, 
    QLabel, 
    QHBoxLayout,
    QPushButton,
    QWidget
    )
import sys

app = QApplication([])

window = QWidget()
window.setWindowTitle("Tugas 1 Kriptografi & Koding")
window.setGeometry(100, 100, 280, 80)
helloMsg = QLabel("<h1>Welcome to Tugas 1 Kriptografi & Koding</h1>", parent=window)
helloMsg.move(60, 15)

layout = QHBoxLayout()
layout.addWidget(QPushButton("Vigenere"))
layout.addWidget(QPushButton("Extended Vigenere"))
layout.addWidget(QPushButton("Playfair"))
layout.addWidget(QPushButton("One-Time Pad"))
window.setLayout(layout)

window.show()
sys.exit(app.exec())