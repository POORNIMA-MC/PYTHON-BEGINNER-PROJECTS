from tkinter import Tk
from tkinter import Label
import time
import sys

root = Tk()
root.title("CLOCK")


def present_time(): 
    display_time = time.strftime("%I: %M: %S %p")
    digi_clock.config(text = display_time,  image = "E:\Screenshot (17).png")
    digi_clock.after(200,present_time)

digi_clock = Label(root, font = ("arial",150),bg = "pink",fg= "black")
digi_clock.pack()

present_time()
root.mainloop()