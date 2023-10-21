from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from random import randint

dodatok=QApplication([])
window = QWidget()
window.setWindowTitle("Calculator")
window.resize(500,500)
window.move(300,150)
window.show()
dodatok.exec_()