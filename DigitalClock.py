import os

os.environ['TCL_LIBRARY'] = r'C:\Users\USER\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\USER\AppData\Local\Programs\Python\Python313\tcl\tk8.6'

from tkinter import Tk, Label
import time

root = Tk()
root.title("Digital Clock")

def present_time():
    display_time = time.strftime("%I:%M:%S %p")
    digi_clock.config(text=display_time)
    digi_clock.after(200, present_time)

digi_clock = Label(
    root,
    font=("arial", 100),
    bg="green",
    fg="black"
)

digi_clock.pack()

present_time()

root.mainloop()