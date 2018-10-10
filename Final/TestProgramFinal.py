import tkinter as tk
# import camera
# import cozmo

counter = 5
def counter_label(label):
  counter = 5
  def count():
    global counter
    #counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
    counter-=1
    if counter==0:
      counter="Smile!!!"
      # cozmo.run_program(camera.cozmo_face_mirror)

  count()

def getvalue(event):
    print(nameentry.get())
 

root=tk.Tk()
startup=tk.Frame(root)#1st page
scores=tk.Frame(root)#score page
loadingpage=tk.Frame(root)#picturepage
namepage= tk.Frame(root)#entry name

def raise_frame(frame):
    frame.tkraise()

for f in (startup,scores,loadingpage,namepage):
    f.grid(row=0, column=0, sticky="news")

##Startup
photo = tk.PhotoImage(file="1.png")
label2= tk.Label(startup, image=photo)
label2.grid(row=0)

title = tk.Label(startup, text="Cozmo the Friendly Robot")
title.config(font="System, 50", padx="300")
title.grid(row=1)

playbutton = tk.Button(startup, text="Lets Play", command=lambda:raise_frame(namepage))
playbutton.config(font="System, 30", pady="10")
playbutton.grid(row=2)

scorebutton = tk.Button(startup, text="Scores", command=lambda:raise_frame(scores))
scorebutton.config(font="System, 30", pady="10")
scorebutton.grid(row=3)


##Scores
scoreslabel= tk.Label(scores, text="Scores")
scoreslabel.config(font="System, 50", padx=300)
scoreslabel.grid(row=0, sticky="news")

backbutton1= tk.Button(scores, text="Back", pady="10", padx="10", command=lambda:raise_frame(startup))
backbutton1.config(font="System,30")
backbutton1.grid(row=1)

##Name Page
name=tk.Label(namepage, text="Please Enter your Name")
name.config(font="System, 50", padx=300)
name.grid(row=0)

nameentry= tk.Entry(namepage)
nameentry.grid(row=1)


nextbutton= tk.Button(namepage, text="Next", command=lambda:raise_frame(loadingpage))
nextbutton.bind("<Button-1>", getvalue)
nextbutton.config(font="System, 30")
nextbutton.grid(row=2)


backbutton2= tk.Button(namepage, text="Back", command=lambda:raise_frame(startup))
backbutton2.config(font="System, 30")
backbutton2.grid(row=3)

##Loading Page
letsgotext= tk.Label(loadingpage, text="Lets Play!!!")
letsgotext.config(font="System, 50", padx=300)
letsgotext.grid(row=0, sticky="news")
countinglabel = tk.Label(loadingpage)
# nextbutton.bind("<Button-1>", counter_label(countinglabel))
countinglabel.config(font="System, 150")
countinglabel.grid(row=1, sticky="news")


raise_frame(startup)
root.mainloop()