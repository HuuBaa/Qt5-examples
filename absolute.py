# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/10/20 15:55'

import sys
from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('label 1', self)
        label1.move(10, 10)

        label2 = QLabel('label 2', self)
        label2.move(30, 30)

        label3 = QLabel('label 3', self)
        label3.move(60, 60)

        self.setWindowTitle('absolute')
        self.setGeometry(300, 300, 300, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
