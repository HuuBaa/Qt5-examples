# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/10/22 17:36'

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QTextEdit, QWidget, QGridLayout, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        title = QLabel('title')
        author = QLabel('author')
        preview = QLabel('preview')

        tEditor = QLineEdit()
        authorEditor = QLineEdit()
        previewEditor = QTextEdit()

        gridLayout = QGridLayout()
        gridLayout.setSpacing(10)
        self.setLayout(gridLayout)

        gridLayout.addWidget(title, 1, 0)
        gridLayout.addWidget(tEditor, 1, 1)

        gridLayout.addWidget(author, 2, 0)
        gridLayout.addWidget(authorEditor, 2, 1)

        gridLayout.addWidget(preview, 3, 0)
        gridLayout.addWidget(previewEditor, 3, 1, 2, 1)

        self.setGeometry(300, 300, 300, 400)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
