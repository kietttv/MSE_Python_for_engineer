import socket
import threading

# Cấu hình client
HOST = '10.26.16.209'  # Địa chỉ localhost
PORT = 7006  

# Tạo socket client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive_messages():
    """Nhận tin nhắn từ server."""
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Đã mất kết nối với server.")
            client.close()
            break

def send_messages():
    """Gửi tin nhắn tới server."""
    alias = input("Chọn biệt danh của bạn: ")
    client.send(alias.encode('utf-8'))
        
    while True:
        message = input()
        if message.lower() == "exit":
            client.close()
            break
        client.send(f"{alias}: {message}".encode('utf-8'))

# Tạo luồng để nhận và gửi tin nhắn đồng thời
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()