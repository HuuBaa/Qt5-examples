# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/10/20 19:56'


import sys
from PyQt5.QtWidgets import QPushButton,QApplication,QHBoxLayout,QVBoxLayout,QWidget

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        okButton=QPushButton('确认')
        cancelButton = QPushButton('取消')

        hLayout=QHBoxLayout()
        hLayout.addStretch(1)
        hLayout.addWidget(okButton)
        hLayout.addWidget(cancelButton)

        vLayout=QVBoxLayout()
        vLayout.addStretch(1)
        vLayout.addLayout(hLayout)

        self.setLayout(vLayout)

        self.setWindowTitle('boxlayout')
        self.setGeometry(300,300,300,300)
        self.show()


if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())