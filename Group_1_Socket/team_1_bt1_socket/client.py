#Nhóm 1
#Lê Thành Nhân
#Lưu Phạm Anh Kiệt
#Nguyễn Nhất Chính
#Trương Văn Tuấn Kiệt
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Client configuration
HOST = '192.168.23.119'
PORT = 12345

# Client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Flag to indicate if the client is exiting or if a valid name is set
is_exiting = False
is_name_set = False  # This flag checks if the chat name has been set

# Function to receive messages
def receive_messages():
    global is_exiting, is_name_set
    while True:
        if is_exiting:
            break  # Exit the loop if the client is exiting
        try:
            message = client_socket.recv(1024).decode()
            if message == "{quit}":
                client_socket.close()
                root.quit()
                break
            elif message.startswith("NameError:"):
                # Name is already taken or invalid
                chat_display.config(state=tk.NORMAL)
                chat_display.insert(tk.END, "Server: " + message + "\n")
                chat_display.config(state=tk.DISABLED)
                chat_display.see(tk.END)
            else:
                # Valid name confirmed or new chat message
                if not is_name_set:
                    is_name_set = True
                    chat_display.config(state=tk.NORMAL)
                    chat_display.insert(tk.END, "Server: Welcome, " + message + "\n")
                    chat_display.config(state=tk.DISABLED)
                    chat_display.see(tk.END)
                else:
                    chat_display.config(state=tk.NORMAL)
                    chat_display.insert(tk.END, message + "\n")
                    chat_display.config(state=tk.DISABLED)
                    chat_display.see(tk.END)  # Auto-scroll to the latest message
        except OSError:
            break  # Exit if the socket is closed

# Function to send messages
def send_message():
    global is_name_set
    message = message_entry.get()
    if message:  # Check if message is not empty
        message_entry.delete(0, tk.END)  # Clear entry box after sending
        if not is_name_set:
            # Send the name to the server for validation
            client_socket.send(message.encode())
        else:
            # Send regular chat message
            chat_display.config(state=tk.NORMAL)
            chat_display.insert(tk.END, "You: " + message + "\n")
            chat_display.config(state=tk.DISABLED)
            chat_display.see(tk.END)  # Auto-scroll to the latest message
            if message == "{quit}" or message == "{close}":
                client_socket.send(message.encode())
                on_close()
            else:
                client_socket.send(message.encode())

# Function to handle closing the application
def on_close():
    global is_exiting
    is_exiting = True  # Set exiting flag
    try:
        client_socket.send("{quit}".encode())  # Notify server that client is quitting
    except OSError:
        pass  # Socket might already be closed
    client_socket.close()  # Close the client socket
    root.quit()  # Close the GUI window

# GUI setup
root = tk.Tk()
root.title("Chat Client")

# Chat display area
chat_display = scrolledtext.ScrolledText(root, state=tk.DISABLED, width=60, height=20)
chat_display.grid(row=0, column=0, columnspan=2)

# Message entry field
message_entry = tk.Entry(root, width=70)
message_entry.grid(row=1, column=0)
message_entry.bind("<Return>", lambda event: send_message())  # Enter key to send

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=1, column=1)

# Display initial message for name entry
chat_display.config(state=tk.NORMAL)
chat_display.insert(tk.END, "Server: Please enter your chat name to start.\n")
chat_display.config(state=tk.DISABLED)

# Start receiving thread
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Override the close button behavior
root.protocol("WM_DELETE_WINDOW", on_close)

# Start the GUI event loop
root.mainloop()
