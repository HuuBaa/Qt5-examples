# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/10/18 21:39'

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 200, 100)
        self.setWindowTitle('confirm me')
        self.show()

    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self, '确认', '你确定退出吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
