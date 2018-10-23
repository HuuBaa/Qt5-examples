# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/10/18 20:34'

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        qbtn=QPushButton('quit',self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(40,10)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('click and quit')
        self.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())