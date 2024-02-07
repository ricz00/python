# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 10:57:22 2024

@author: AICS LAB2
"""
import sys
import PyQt5
from PyQt5.QtWidgets import *
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Blacklist")
        self.resize(200,200)
        
        self.label = QLabel(self) 
        self.label.setText("time is gold study hard")
        self.label.setGeometry(250,250,100,100) 
        
        self.button = QPushButton(self)
        self.button.setText("Click me")
        self.button.clicked.connect(self.buttonMethod)
        
    def buttonMethod(self):
       self.label.setText("Hello")      
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    app.exec() 
