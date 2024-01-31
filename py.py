# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def fibo(limit):
    num1 = 0
    num2 = 1
    for i in range (limit):
        temp = num1
        num1 = temp + num2
        num2 = temp
        print (temp)
        
if __name__ == "_main_":    
    fibo(6)        
