# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/10/19 16:24'

import sys
from PyQt5.QtWidgets import QMainWindow,QApplication

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('status bar')
        self.setGeometry(300,300,300,300)
        self.statusBar().showMessage('冲鸭！')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())