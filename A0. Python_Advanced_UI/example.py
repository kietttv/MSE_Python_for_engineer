import tkinter as tk
from tkinter import *

window = Tk()
window.title("Welcome to my app")
window.geometry("350x200")

lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

def ok_clicked():
    lbl.configure(text="Button Ok was clicked!!")

def cancel_clicked():
    lbl.configure(text="Button Cancel was clicked!!")

btn_Ok = Button(window, text="Ok", command=ok_clicked, justify="left", width=50, bg="green")
btn_Cancel = Button(window, text="Cancel", command=cancel_clicked, justify="left", width=50, bg="yellow", fg='red')

btn_Ok.grid(column=0, row=1)  # Place below the label
btn_Cancel.grid(column=0, row=2)  # Place below the "Ok" button

window.mainloop()
