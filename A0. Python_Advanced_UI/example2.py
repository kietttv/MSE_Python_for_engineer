import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Simple Interface")
window.geometry("300x200")  # Set the window size

# Create a label
lbl = tk.Label(window, text="Enter your name:")
lbl.pack(pady=10)

# Create a text entry widget
entry = tk.Entry(window, width=30)
entry.pack(pady=5)

# Function to display the entered text
def display_text():
    user_text = entry.get()
    lbl_result.config(text=f"Hello, {user_text}!")

# Function to clear the text
def clear_text():
    entry.delete(0, tk.END)
    lbl_result.config(text="")

entry.bind("<Enter>", display_text)    

# Create buttons
btn_display = tk.Button(window, text="Display", command=display_text, bg="blue", fg="white")
btn_display.pack(pady=5)

btn_clear = tk.Button(window, text="Clear", command=clear_text, bg="red", fg="white")
btn_clear.pack(pady=5)

# Create a label to display the result
lbl_result = tk.Label(window, text="")
lbl_result.pack(pady=10)

# Run the application
window.mainloop()
