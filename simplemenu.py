# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/10/19 19:03'

import sys
from PyQt5.QtWidgets import QApplication, QAction, qApp, QMainWindow
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('qq.png'), '&Exit', self)
        exitAction.setShortcut('CTRL+Q')
        exitAction.setStatusTip('退出程序')
        exitAction.triggered.connect(qApp.quit)

        exitAction2 = QAction('&wocao', self)
        exitAction2.setShortcut('CTRL+W')
        exitAction2.setStatusTip('wocao')
        exitAction2.triggered.connect(qApp.quit)

        self.statusBar()

        menuBar = self.menuBar()
        editMenu = menuBar.addMenu('&编辑')
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(exitAction2)

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('simple menu')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
