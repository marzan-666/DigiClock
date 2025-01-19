from tkinter import Tk
from tkinter import Label
import time

root = Tk()
root.title("Clock")

def present_time():
    display_time = time.strftime("%I:%M:%S %p")
    #display_time = time.strftime("%H:%M:%S %p") %H is for 24hr format
    digi_clock.config(text=display_time)
    digi_clock.after(200,present_time)



digi_clock = Label(root, font= ("arial",150),bg="gray", fg="black")
digi_clock.pack()

present_time()

root.mainloop()

