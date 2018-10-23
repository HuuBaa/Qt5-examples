# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/10/20 13:20'

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp,QMenu
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        qAct = QAction(QIcon('qq.png'), 'Exit', self)
        qAct.setShortcut('Ctrl+Q')
        qAct.triggered.connect(qApp.quit)

        self.statusBar().showMessage('sd')
        self.menuBar().addMenu(QMenu('ds',self))

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(qAct)

        self.setWindowTitle('context menu')
        self.setGeometry(300, 300, 400, 400)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
