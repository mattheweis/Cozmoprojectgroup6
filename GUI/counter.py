# import time

# def countdown():
#     countDown = 3
#     while (countDown >= 0):
#         print(countDown)
#         time.sleep(1)
#         countDown = countDown - 1
#         if countDown == 0:
#             print("Smile!")
#             break
import tkinter as tk

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.label = tk.Label(self, text="", width=10)
        self.label.pack()
        self.remaining = 0
        self.countdown(10)

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.label.configure(text="Smile!!!")
        else:
            self.label.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()