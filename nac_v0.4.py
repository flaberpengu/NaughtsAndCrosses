import random
import tkinter as tk

root = tk.Tk()
root.title='Naughts and Crosses'
root.geometry('300x300')

global buttons
buttons = []

global n_or_c
n_or_c = 'n'

def win():
    root.destroy()
    main=tk.Tk()
    main.title='Winner'
    main.geometry('200x200')
    label1 = tk.Label(main,text='Congratulations',width=15,height=3)
    label1.grid(row=0,column=0)
    label2 = tk.Label(main,text='You won!',width=10,height=3)
    label2.grid(row=1,column=0)

def check_r_and_c():
    global buttons
    winner = False
    x_or_o = 'X'
    for g in range(2):
        for e in range(0,6,2):
            num_in_row = 0
            num_in_col = 0
            for f in range(0,6,2):
                if buttons[e][f].cget('text') == x_or_o:
                    num_in_row += 1
                if buttons[f][e].cget('text') == x_or_o:
                    num_in_col += 1
            if num_in_col == 3 or num_in_row == 3:
                winner = True
        x_or_o = 'O'
    if winner == True:
        win()

def check_win():
    check_r_and_c()

def place_symbol(row,column):
    global n_or_c
    global buttons
    if n_or_c == 'n':
        buttons[row][column].configure(text='O',state=tk.DISABLED,fg='black')
        n_or_c = 'c'
    elif n_or_c == 'c':
        buttons[row][column].configure(text='X',state=tk.DISABLED,fg='black')
        n_or_c = 'n'
    check_win()
    

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
