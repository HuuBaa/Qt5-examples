# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/10/19 15:33'

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('居中')
        self.resize(300, 300)
        self.center()
        self.show()

    def center(self):
        cp = QDesktopWidget().availableGeometry().center()  # 桌面中心
        qr = self.frameGeometry()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
