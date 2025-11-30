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
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.expression  = ""
        self.Handle_buttons()
        self.handle_exit()

    def Handle_buttons(self):
        buttons_list = [self.b0, self.b1, self.b2, self.b3, self.b4,
                        self.b5, self.b6, self.b7, self.b8, self.b9]
        for btn in buttons_list:
            btn.clicked.connect(self.add_num)

        self.bc.clicked.connect(self.clear_display)
        self.b_divide.clicked.connect(lambda:self.add_operator('/'))
        self.b_plus.clicked.connect(lambda:self.add_operator('+'))
        self.b_times.clicked.connect(lambda:self.add_operator('*'))
        self.b_minus.clicked.connect(lambda:self.add_operator('-'))
        self.b_equal.clicked.connect(lambda:self.calculate())

    def add_num(self):
        btn = self.sender()
        self.expression += btn.text()
        self.output_lable.setText(self.expression)

    def add_operator(self, op):
        self.expression += op
        self.output_lable.setText(self.expression)

    def clear_display(self):
        self.expression = ""
        self.output_lable.clear()

    def calculate(self):
        try:
            self.expression = self.output_lable.text()
            result = eval(self.expression)
            self.expression = str(result)
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