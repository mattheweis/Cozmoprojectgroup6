import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame2 = tk.Frame(root)

def raise_frame(frame):
    frame.tkraise()

for f in (frame, frame2):
    f.grid(row=0, column=0, sticky='news')

#frame
button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                text="Hello",
                command=lambda:raise_frame(frame2))
slogan.pack(side=tk.LEFT)

#frame2
button2 = tk.Button(frame2, 
                   text="QUIT", 
                   fg="red",
                   command=quit).pack()

raise_frame(frame)
root.mainloop()