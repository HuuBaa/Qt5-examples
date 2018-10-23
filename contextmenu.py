# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/10/20 12:31'

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, qApp


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        menu = self.menuBar()
        menu.addMenu('dd')
        self.setWindowTitle('context menu')
        self.setGeometry(300, 300, 400, 400)
        self.show()

    def contextMenuEvent(self, QContextMenuEvent):
        cmenu = QMenu(self)
        cmenu.addAction('new')
        cmenu.addAction('open')
        quitAct = cmenu.addAction('quit')
        action = cmenu.exec_(self.mapToGlobal(QContextMenuEvent.pos()))

        if action == quitAct:
            qApp.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
