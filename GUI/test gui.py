from tkinter import *

canvas = Tk()#makes window
# thelabel = Label(canvas,text="Hello")
# thelabel.pack()#place where ever
#fg means text color, bg is background color

topframe = Frame(canvas)#makes invisible container
topframe.pack()
bottomframe = Frame(canvas)
bottomframe.pack(side=BOTTOM)

button1= Button(topframe, text = "Button 1", fg = "red")#(frame, text on button, color)
button2= Button(topframe, text = "Button 2", fg = "blue")#(frame, text on button, color)
button3= Button(topframe, text = "Button 3", fg = "green")#(frame, text on button, color)
button4= Button(bottomframe, text = "Button 4", fg = "purple")#(frame, text on button, color)

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

canvas.mainloop()



