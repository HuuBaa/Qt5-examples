# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/10/22 19:18'

import sys
from PyQt5.QtCore import pyqtSignal,QObject
from PyQt5.QtWidgets import QApplication,QPushButton,QMainWindow


class CustomSignal(QObject):
    '''
    自定义信号
    '''
    closeMe=pyqtSignal()

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.c=CustomSignal()
        self.c.closeMe.connect(self.close)

        btn1=QPushButton('按键1',self)
        btn1.move(10,10)

        btn2 = QPushButton('按键2', self)
        btn2.move(10,50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()
        self.setGeometry(300, 300, 450, 450)
        self.setWindowTitle('sender')
        self.show()

    def buttonClicked(self):
        sender=self.sender()
        self.statusBar().showMessage(f'你按的是{sender.text()}')

    def mousePressEvent(self, event):
        self.c.closeMe.emit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
