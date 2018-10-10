from tkinter import *


class whatever:
    def __init__(self, master):#no need to call the function it gets called automatically #master means root
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command= frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("WOWWWWWWW")





root=Tk()
b= whatever(root)
root.mainloop()