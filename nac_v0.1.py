import random
import tkinter as tk

root = tk.Tk()
root.title='Naughts and Crosses'
root.geometry('300x300')

spaces = []
for a in range(5):
    for b in range(5):
        button = tk.Button(text='',width=5,height=3)
        button.grid(row=a,column=b)
        spaces.append(button)
for c in range(1,5,2):
    for d in range(5):
        spaces[c][d].configure(colour='black',state=tk.DISABLED,relief='groove')
for e in range(1,5,2):
    for f in range(5):
        spaces[f][e].configure(colour='black',state=tk.DISABLED,relief='groove')
