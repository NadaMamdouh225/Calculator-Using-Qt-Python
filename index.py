#!/usr/bin/env python3
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

import sys
import os
from os import path


FORM_CLASS,_ = loadUiType(path.join(path.dirname(__file__),"main.ui"))


class mainapp(QMainWindow ,FORM_CLASS):
    def __init__(self,parent = None):
        super(mainapp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_numbers()
        self.handle_exit()

    def Handle_numbers(self):
        self.b1.clicked.connect(lambda:self.display_num('1'))
        self.b2.clicked.connect(lambda:self.display_num('2'))
        self.b3.clicked.connect(lambda:self.display_num('3'))
        self.b4.clicked.connect(lambda:self.display_num('4'))
        self.b5.clicked.connect(lambda:self.display_num('5'))
        self.b6.clicked.connect(lambda:self.display_num('6'))
        self.b7.clicked.connect(lambda:self.display_num('7'))
        self.b8.clicked.connect(lambda:self.display_num('8'))
        self.b9.clicked.connect(lambda:self.display_num('9'))
        self.b0.clicked.connect(lambda:self.display_num('0'))
        self.bc.clicked.connect(lambda:self.display_num('C'))
        self.b_divide.clicked.connect(lambda:self.display_num('/'))
        self.b_plus.clicked.connect(lambda:self.display_num('+'))
        self.b_times.clicked.connect(lambda:self.display_num('*'))
        self.b_minus.clicked.connect(lambda:self.display_num('-'))
        self.b_equal.clicked.connect(lambda:self.calculate())

    def display_num(self, num):
        if num == 'C':
            self.output_lable.setText('')
        else:
            if (self.output_lable.text() == '' and num == '0'):
                self.output_lable.setText('')
            else:
                num = self.output_lable.text()+num
                self.output_lable.setText(num)

    def calculate(self):
        try:
            expression = self.output_lable.text()
            result = eval(expression)
            self.output_lable.setText(str(result))
        except Exception as e:
            self.output_lable.setText("Error")
                    
    def handle_exit(self):
        self.Exit.triggered.connect(lambda: QApplication.quit())



def main():
    app = QApplication(sys.argv)
    window = mainapp()
    window.show()
    app.exec_()

if __name__== '__main__':
    main()