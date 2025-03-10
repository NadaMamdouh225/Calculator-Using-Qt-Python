#!/usr/bin/env python3
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

import sys
import os
from os import path
import urllib.request

FORM_CLASS,_ = loadUiType(path.join(path.dirname(__file__),"main.ui"))


class mainapp(QMainWindow ,FORM_CLASS):
    def __init__(self,parent = None):
        super(mainapp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_numbers()

    def Handle_numbers(self):
        self.b1.clicked.connect(lambda:self.display_num('1'))
        self.b2.clicked.connect(lambda:self.display_num('2'))

    def display_num(self, b_num):
        self.output_lable.setText(b_num)


def main():
    app = QApplication(sys.argv)
    window = mainapp()
    window.show()
    app.exec_()

if __name__== '__main__':
    main()