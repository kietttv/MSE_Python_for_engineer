import socket
import threading
from tkinter import Tk, Text, Entry, Button, Scrollbar, END, DISABLED, NORMAL, Toplevel

# Cấu hình client
HOST = '10.26.16.209'  # Địa chỉ server
PORT = 7006            # Cổng server

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

alias = ""  # Biến lưu biệt danh


def receive_messages():
    """Nhận tin nhắn từ server."""
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            chat_area.config(state=NORMAL)
            chat_area.insert(END, message + '\n')
            chat_area.config(state=DISABLED)
            chat_area.see(END)
        except:
            chat_area.config(state=NORMAL)
            chat_area.insert(END, "Đã mất kết nối với server.\n")
            chat_area.config(state=DISABLED)
            client.close()
            break


def send_message():
    """Gửi tin nhắn tới server."""
    message = message_input.get()
    if message.lower() == "exit":
        client.close()
        root.destroy()
        return
    if message.strip() != "":
        client.send(f"{alias}: {message}".encode('utf-8'))
        chat_area.config(state=NORMAL)
        chat_area.insert(END, f"Bạn: {message}\n")
        chat_area.config(state=DISABLED)
        chat_area.see(END)
        message_input.delete(0, END)


def submit_alias():
    """Xử lý nhập alias và mở giao diện chat."""
    global alias
    alias = alias_input.get()
    if alias.strip() != "":
        client.send(alias.encode('utf-8'))  # Gửi biệt danh đến server
        alias_window.destroy()  # Đóng cửa sổ nhập tên
        create_chat_gui()  # Tạo giao diện chat chính


def create_alias_gui():
    """Tạo giao diện nhập tên."""
    global alias_window, alias_input

    alias_window = Tk()
    alias_window.title("Nhập Biệt Danh")

    label = Text(alias_window, height=2, width=30, bg="lightgray", fg="black", font=("Arial", 12))
    label.insert(END, "Nhập biệt danh của bạn:")
    label.config(state=DISABLED)
    label.pack(pady=10)

    alias_input = Entry(alias_window, width=30, font=("Arial", 12))
    alias_input.pack(pady=5)
    alias_input.bind('<Return>', lambda event: submit_alias())

    submit_button = Button(alias_window, text="Bắt đầu chat", command=submit_alias, bg="blue", fg="white", font=("Arial", 12))
    submit_button.pack(pady=10)

    alias_window.mainloop()


def create_chat_gui():
    """Tạo giao diện chat chính."""
    global root, chat_area, message_input

    root = Tk()
    root.title("Chat App")

    # Khung hiển thị tin nhắn
    chat_area = Text(root, wrap='word', state=DISABLED, bg='white', fg='black', font=('Arial', 12))
    chat_area.grid(row=0, column=0, columnspan=2, sticky="nsew")

    # Thanh cuộn
    scrollbar = Scrollbar(root, command=chat_area.yview)
    scrollbar.grid(row=0, column=2, sticky='ns')
    chat_area['yscrollcommand'] = scrollbar.set

    # Ô nhập tin nhắn
    message_input = Entry(root, width=50, bg='lightgray', font=('Arial', 12))
    message_input.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    message_input.bind('<Return>', lambda event: send_message())

    # Nút gửi tin nhắn
    send_button = Button(root, text="Gửi", command=send_message, bg='blue', fg='white', font=('Arial', 12))
    send_button.grid(row=1, column=1, padx=5, pady=5)

    # Đặt lại kích thước lưới
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Chạy luồng nhận tin nhắn
    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

    root.mainloop()


# Khởi chạy giao diện nhập tên
create_alias_gui()
