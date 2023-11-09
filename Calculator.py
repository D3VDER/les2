from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from random import randint

dodatok=QApplication([])
window = QWidget()
window.setWindowTitle("Calculator")
window.resize(500,500)
window.move(300,150)

def clear1():
    LineEdit.setText("")

def suma():
    global f1
    global dia
    f1 = int(LineEdit.text())
    LineEdit.setText("")
    dia = 1
def minus1():
    global f1
    global dia
    f1 = int(LineEdit.text())
    LineEdit.setText("")
    dia = 2
def mnoz():
    global f1
    global dia
    f1 = int(LineEdit.text())
    LineEdit.setText("")
    dia = 3
def dily():
    global f1
    global dia
    f1 = int(LineEdit.text())
    LineEdit.setText("")
    dia = 4

def doriv1():
    f2 = int(LineEdit.text())
    if dia == 1:
        LineEdit.setText(str(f1+f2))
    if dia == 2:
        LineEdit.setText(str(f1-f2))
    if dia == 3:
        LineEdit.setText(str(f1*f2))
    if dia == 4:
        if f2==0:
            LineEdit.setText(str("ERROR"))  
        else:  
            LineEdit.setText(str(f1/f2))


def zero():
    LineEdit.setText(LineEdit.text()+"0")
def one():
    LineEdit.setText(LineEdit.text()+"1")
def two():
    LineEdit.setText(LineEdit.text()+"2")
def three():
    LineEdit.setText(LineEdit.text()+"3")
def four():
    LineEdit.setText(LineEdit.text()+"4")
def five():
    LineEdit.setText(LineEdit.text()+"5")
def six():
    LineEdit.setText(LineEdit.text()+"6")
def seven():
    LineEdit.setText(LineEdit.text()+"7")
def eight():
    LineEdit.setText(LineEdit.text()+"8")
def nine():
    LineEdit.setText(LineEdit.text()+"9")
LineEdit=QLineEdit()

but = QPushButton()
but.setText("0")

but1 = QPushButton()
but1.setText("1")

but2 = QPushButton()
but2.setText("2")

but3 = QPushButton()
but3.setText("3")

but4 = QPushButton()
but4.setText("4")

but5 = QPushButton()
but5.setText("5")

but6 = QPushButton()
but6.setText("6")

but7 = QPushButton()
but7.setText("7")

but8 = QPushButton()
but8.setText("8")

but9 = QPushButton()
but9.setText("9")

plus = QPushButton()
plus.setText("+")

minus = QPushButton()
minus.setText("-")

pomnoz = QPushButton()
pomnoz.setText("*")

podil = QPushButton()
podil.setText("/")

doriv = QPushButton()
doriv.setText("=")

clear=QPushButton()
clear.setText("Clear")

lineV=QVBoxLayout()


lineH1=QHBoxLayout()
lineH2=QHBoxLayout()
lineH3=QHBoxLayout()
lineH4=QHBoxLayout()
lineH5=QHBoxLayout()

lineH1.addWidget(LineEdit)
lineH2.addWidget(but1)

lineH2.addWidget(but2)
lineH2.addWidget(but3)
lineH2.addWidget(plus)

lineH3.addWidget(but4)
lineH3.addWidget(but5)
lineH3.addWidget(but6)
lineH3.addWidget(minus)

lineH4.addWidget(but7)
lineH4.addWidget(but8)
lineH4.addWidget(but9)
lineH4.addWidget(pomnoz)

lineH5.addWidget(but)
lineH5.addWidget(podil)
lineH5.addWidget(doriv)
lineH5.addWidget(clear)

lineV.addLayout(lineH1)
lineV.addLayout(lineH2)
lineV.addLayout(lineH3)
lineV.addLayout(lineH4)
lineV.addLayout(lineH5)


plus.clicked.connect(suma)
clear.clicked.connect(clear1)
but1.clicked.connect(one)
but2.clicked.connect(two)
but3.clicked.connect(three)
but4.clicked.connect(four)
but5.clicked.connect(five)
but6.clicked.connect(six)
but7.clicked.connect(seven)
but8.clicked.connect(eight)
but9.clicked.connect(nine)
minus.clicked.connect(minus1)
pomnoz.clicked.connect(mnoz)
podil.clicked.connect(dily)
doriv.clicked.connect(doriv1)
but.clicked.connect(zero)

window.setLayout(lineV)
window.show()
dodatok.exec_()
