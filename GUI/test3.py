from tkinter import *

root= Tk()

def printname(event):
    print("Hello People!!!!!!")

button1= Button(root, text= "Print Me")
button1.bind("<Button-1>", printname)
button1.pack()

root.mainloop()