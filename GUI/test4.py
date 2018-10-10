from tkinter import *

root= Tk()

def leftclick(event):
    print("left")

def rightclick(event):
    print("right")

frame= Frame(root, width=300, height=300)
frame.bind("<Button-1>",leftclick)
frame.bind("<Button-3>",rightclick)
frame.pack()
root.mainloop()