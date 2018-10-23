# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/10/20 13:58'

import sys
from PyQt5.QtWidgets import QAction,QTextEdit,QApplication,QMenu,QMainWindow
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        textEditor=QTextEdit()
        self.setCentralWidget(textEditor)

        exitAct=QAction(QIcon('qq.png'),'退出',self)
        exitAct.setShortcut('CTRL+Q')
        exitAct.setStatusTip('Exit')
        exitAct.triggered.connect(self.close)

        statusBar = self.statusBar()

        menu=QMenu('File',self)
        menu.addAction(exitAct)

        menuBar = self.menuBar()
        menuBar.addMenu(menu)

        toolBar=self.addToolBar('离开')
        toolBar.addAction(exitAct)

        self.setGeometry(300,300,500,500)
        self.setWindowTitle('main')
        self.show()


if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())