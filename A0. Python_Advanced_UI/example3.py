from tkinter import *

window = Tk()
window.title("My Windows App")
window.geometry("350x200")

# Create a label prompting the user
lbl = Label(window, text="Xin mời nhập một chuỗi bất kỳ")
lbl.grid(column=0, row=0)

# Create a label for displaying results
lbl1 = Label(window, text="")
lbl1.grid(column=0, row=2)

# Create a Textbox
txt = Entry(window, width=20)
txt.grid(column=0, row=1)  # Adjust the position
txt.focus()  # Set the focus to this textbox

# Function to handle button click
def ok_clicked():
    res = "Chuỗi đã nhập: " + txt.get()
    lbl1.configure(text=res)

# Create a Button
btn = Button(window, text="OK", command=ok_clicked)
btn.grid(column=1, row=1)  # Adjust the position

window.mainloop()