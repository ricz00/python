# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 11:03:46 2024

@author: AICS LAB2
"""

import sys
import PyQt5
from PyQt5.QtWidgets import *

class Account(QDialog):
    def __init__(self):
        super(Account,self).__init__()
        AccountLayout = QGridLayout(self)
        
        self.usernameLabel = QLabel()
        self.pinLabel = QLabel()
        self.userLineEdit = QLineEdit()
        self.pinLineEdit = QLineEdit()
        self.pinLineEdit.setEchoMode(QLineEdit.Password)
        self.loginButton = QPushButton()
        
        AccountLayout.addWidget(self.usernameLabel,0,0,1,1)
        AccountLayout.addWidget(self.pinLabel,1,0,1,1)
        AccountLayout.addWidget(self.userLineEdit,0,1,1,3)
        AccountLayout.addWidget(self.pinLineEdit,1,1,1,3)
        AccountLayout.addWidget(self.loginButton,2,1,1,2)
        
        self.usernameLabel.setText("Username: ")
        self.pinLabel.setText("Pin: ")
        self.loginButton.setText("login")
        
        self.loginButton.clicked.connect(self.Handlelogin)
        
    def Handlelogin(self):
        if(self.userLineEdit.text() =="Admin" 
           and self.pinLineEdit.text() == "password"):
            print("Login Success!") 
        else:
            print("Login Failed!")
        
if __name__== "__main__":
    app = QApplication(sys.argv)
    dialog = Account()
    dialog.show()
    app.exec()
        