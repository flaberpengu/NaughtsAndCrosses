import random
import tkinter as tk

root = tk.Tk()
root.title='Naughts and Crosses'
root.geometry('300x300')

global buttons
buttons = []

def build_GUI():
    global buttons
    for a in range(5):
        temp = []
        for b in range(5):
            button=tk.Button(text='',width=5,height=3)
            button.grid(column=b,row=a)
            temp.append(button)
        buttons.append(temp)
    for c in range(1,5,2):
       for d in range(5):
           buttons[c][d].configure(bg='black',state=tk.DISABLED,relief='groove')
           buttons[d][c].configure(bg='black',state=tk.DISABLED,relief='groove')

build_GUI()

##buttons = []
##for a in range(5):
##    temp = []
##    for b in range(5):
##        button = tk.Button(text='',width=5,height=3)
##        button.grid(row=a,column=b)
##        temp.append(button)
##    buttons.append(button)
##
##buttons[0][1].configure(colour='black',state=tk.DISABLED,relief='groove')
##for c in range(1,5,2):
##    for d in range(5):
##        buttons[c][d].configure(colour='black',
##                                state=tk.DISABLED,
##                                relief='groove')
##for e in range(1,5,2):
##    for f in range(5):
##        buttons[f][e].configure(colour='black',
##                                state=tk.DISABLED,
##                                relief='groove')
