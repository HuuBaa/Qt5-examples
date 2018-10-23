# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/10/19 20:14'

import sys
from PyQt5.QtWidgets import QAction,QApplication,QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.statusBar=self.statusBar()
        self.statusBar.showMessage('cool')

        viewStatusAct=QAction('显示状态栏',self)
        viewStatusAct.setCheckable(True)
        viewStatusAct.setStatusTip('状态栏信息')
        viewStatusAct.setChecked(True)
        viewStatusAct.triggered.connect(self.toggleStatus)

        menuBar=self.menuBar()

        viewMenu=menuBar.addMenu('view')
        viewMenu.addAction(viewStatusAct)

        self.setWindowTitle('check menu')
        self.setGeometry(300,300,300,300)
        self.show()

    def toggleStatus(self,state):
        print(state)
        if state:
            self.statusBar.show()
        else:
            self.statusBar.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())