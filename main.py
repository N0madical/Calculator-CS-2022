from tkinter import *
import time
master = Tk()
#960x540

screen_width = master.winfo_width()
screen_height = master.winfo_height()
print(screen_height)
print(screen_width)

text = Label(master, text="Hello, world!")

def resize(event):
    text.place(x=(master.winfo_width()) / 2, y=(master.winfo_height()) / 2, anchor=CENTER)

master.bind("<Configure>",resize)
mainloop()
