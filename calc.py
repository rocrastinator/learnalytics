#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 10:42:42 2019

@author: rohan
"""

from tkinter import *
import tkinter as tk
root=tk.Tk()
root.title("Calculator using TK")
root.geometry("400x400")
num1 = Label(root,text = "First Number",height=2).grid(row = 0, column = 0,padx=5, pady=20)  
e1 = Entry(root)
e1.grid(row = 0, column = 1) 
operation = Label(root,text = "operation",height=2).grid(row = 1, column = 0,padx=5, pady=20)
e2 = Entry(root)
e2.grid(row = 1, column = 1)
num2 = Label(root,text = "Second Number",height=2).grid(row = 2, column = 0,padx=5, pady=20)  
e3 = Entry(root)
e3.grid(row = 2, column = 1)
last = Label(root,text = "Result",height=2)
last.grid(row = 10, column = 0,padx=5, pady=20)
last2 = Label(root,text = "",height=2)
last2.grid(row = 10, column = 1,padx=5, pady=20)


def calc():
    x=int(e1.get())
    y=int(e3.get())
    z=e2.get()
    if z== '+':
        r=x+y
        last2.config(text ='addidtion is {}'.format(r))

submit = Button(root, text = "Calculate",height=2,command=calc).grid(row = 8, column = 1)

root.mainloop()