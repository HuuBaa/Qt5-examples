# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/10/18 18:56'

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SanSerif', 10))

        self.setToolTip('这是一个 <b>Qwidget<b/> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('这是一个 <b>QPushButton<b/> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 10)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
