#Nhóm 1
#Lê Thành Nhân
#Lưu Phạm Anh Kiệt
#Nguyễn Nhất Chính
#Trương Văn Tuấn Kiệt
#sử dụng @username để chat riêng với 1 user
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
            elif message.startswith("User "):
                # Hiển thị thông báo người dùng không tìm thấy
                chat_display.config(state=tk.NORMAL)
                chat_display.insert(tk.END, "Server: " + message + "\n")
                chat_display.config(state=tk.DISABLED)
                chat_display.see(tk.END)
            else:
                # Hiển thị tin nhắn từ server
                chat_display.config(state=tk.NORMAL)
                chat_display.insert(tk.END, message + "\n")
                chat_display.config(state=tk.DISABLED)
                chat_display.see(tk.END)
        except:
            print("An error occurred while receiving messages.")
            break

# Function to send messages
def send_message():
    message = message_input.get()
    message_input.delete(0, tk.END)
    if message:
        client_socket.send(message.encode())
        # Hiển thị tin nhắn của chính người dùng
        chat_display.config(state=tk.NORMAL)
        chat_display.insert(tk.END, "You: " + message + "\n")
        chat_display.config(state=tk.DISABLED)
        chat_display.see(tk.END)

# Function to close the client
def on_closing():
    global is_exiting
    is_exiting = True
    client_socket.send("{quit}".encode())
    root.quit()

# GUI setup
root = tk.Tk()
root.title("Chat Client")

chat_display = scrolledtext.ScrolledText(root, state='disabled', width=60, height=20)
chat_display.grid(row=0, column=0, columnspan=2)

message_input = tk.Entry(root, width=70)
message_input.grid(row=1, column=0)
message_input.bind("<Return>", lambda event: send_message())

send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=1, column=1)

root.protocol("WM_DELETE_WINDOW", on_closing)

# Start receiving messages in a separate thread
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

root.mainloop()