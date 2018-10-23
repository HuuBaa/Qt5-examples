# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/10/19 20:14'

import sys
from PyQt5.QtWidgets import QAction, QApplication, QMainWindow, QMenu


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        sub_action = QAction('sub_action', self)
        sub_menu = QMenu('sub_menu', self)  # 创建子菜单
        sub_menu.addAction(sub_action)

        menuBar = self.menuBar()  # 创建菜单栏
        menu = menuBar.addMenu('menu')
        action = QAction('action', self)

        menu.addAction(action)
        menu.addMenu(sub_menu)

        self.setWindowTitle('子菜单')
        self.setGeometry(300, 300, 300, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
