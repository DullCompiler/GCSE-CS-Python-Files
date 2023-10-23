from tkinter import *
import time
testtimer=0
window = Tk()
window.title("GUI test")
window.geometry('350x200')

#label
lbl = Label(window, text="test")
lbl.grid(column=0, row=0)

def clicked():
    lbl.configure(text="Button test: Success")
#button
btn = Button(window, text="Button Test", command=clicked)
btn.grid(column=1, row=0)

window.mainloop()
