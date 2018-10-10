from tkinter import *

def doNothing():
    print("ok ok i won't ......")

root= Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu= Menu(menu)
menu.add_cascade(label="File", menu=subMenu)#Dropdown Menu
subMenu.add_command(label= "New Project", command=doNothing)#items in dropdown
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

root.mainloop()