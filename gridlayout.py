# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/10/20 21:47'

import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        gridLayout = QGridLayout()
        self.setLayout(gridLayout)

        l = ['Cls', '', 'Bck', 'Close',
             '7', '8', '9', '/',
             '4', '5', '6', '*',
             '1', '2', '3', '-',
             '0', '.', '=', '+'
             ]
        coordinate = [(i, j) for i in range(5) for j in range(4)]

        for text, pos in zip(l, coordinate):
            if text == '':
                continue
            qbtn = QPushButton(text, self)
            gridLayout.addWidget(qbtn, *pos)

        self.setGeometry(300, 300, 500, 500)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
