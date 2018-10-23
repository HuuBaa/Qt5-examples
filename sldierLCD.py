# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/10/22 19:18'

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QLCDNumber, QSlider, QWidget, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        x = 0
        y = 0
        text = f'x:{x} y:{y}'
        self.posL = QLabel(text, self)

        lcd = QLCDNumber(self)
        slider = QSlider(Qt.Horizontal, self)
        slider.valueChanged.connect(lcd.display)


        vbox = QVBoxLayout()
        vbox.addWidget(self.posL, 0, Qt.AlignRight)

        vbox.addWidget(lcd)
        vbox.addWidget(slider)

        self.setMouseTracking(True)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 450, 450)
        self.setWindowTitle('Signal and slot')
        self.show()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Escape:
            self.close()

    def mouseMoveEvent(self, QMouseEvent):
        x = QMouseEvent.x()
        y = QMouseEvent.y()
        text = f'x:{x} y:{y}'
        self.posL.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
