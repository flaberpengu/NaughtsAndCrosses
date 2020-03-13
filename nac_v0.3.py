import random
import tkinter as tk

root = tk.Tk()
root.title='Naughts and Crosses'
root.geometry('300x300')

global buttons
buttons = []

global n_or_c
n_or_c = 'n'

def place_symbol(row,column):
    global n_or_c
    global buttons
    if n_or_c == 'n':
        buttons[row][column].configure(text='O',state=tk.DISABLED,fg='black')
        n_or_c = 'c'
    elif n_or_c == 'c':
        buttons[row][column].configure(text='X',state=tk.DISABLED,fg='black')
        n_or_c = 'n'
    

def build_GUI():
    global buttons
    for a in range(5):
        temp = []
        for b in range(5):
            button=tk.Button(text='',width=5,height=3,command=lambda row=a,column=b:place_symbol(row,column))
            button.grid(column=b,row=a)
            temp.append(button)
        buttons.append(temp)
    for c in range(1,5,2):
       for d in range(5):
           buttons[c][d].configure(bg='black',state=tk.DISABLED,relief='groove',height=1)
           buttons[d][c].configure(bg='black',state=tk.DISABLED,relief='groove',width=2)

build_GUI()
