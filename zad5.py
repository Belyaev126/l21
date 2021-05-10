#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *
from random import random


def on_click():
    x = random()
    y = random()
    bt1.place(relx=x, rely=y)


root = Tk()
root['bg'] = 'white'
root.title('crown')
img = PhotoImage(file='crown.png')

bt1 = Button(image=img, command=on_click)
bt1.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
