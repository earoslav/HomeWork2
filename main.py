from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QPushButton,QVBoxLayout
from PyQt5.QtCore import Qt
from random import randint

app = QApplication([])
win = QWidget()
win.resize(300,300)
win.setWindowTitle("Лотерея")
mainLine = QVBoxLayout()

lbl = QLabel("Натисни, щоб взяти участь")
lbl2 = QLabel("?")
lbl3 = QLabel("?")
btn = QPushButton("Випробувати удачу")

mainLine.addWidget(lbl, alignment=Qt.AlignCenter)
mainLine.addWidget(lbl2, alignment=Qt.AlignCenter)
mainLine.addWidget(lbl3, alignment=Qt.AlignCenter)
mainLine.addWidget(btn, alignment=Qt.AlignCenter)

def pushPlay():
    text1 = str(randint(0,10))
    text2 = str(randint(0,10))
    lbl2.setText(text1)
    lbl3.setText(text2)
    if text1 == text2:
        lbl.setText("Ви виграли! Зіграйте знову")
    else:
        lbl.setText("Ви програли! Зіграйте знову")    
btn.clicked.connect(pushPlay)

win.setLayout(mainLine)
win.show()
app.exec()

