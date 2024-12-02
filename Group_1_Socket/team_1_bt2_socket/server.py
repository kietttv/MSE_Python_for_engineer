#Nhóm 1
#Lê Thành Nhân
#Lưu Phạm Anh Kiệt
#Nguyễn Nhất Chính
#Trương Văn Tuấn Kiệt
import socket
import threading

# Server configuration
HOST = '192.168.23.119'  # Localhost for testing
PORT = 12345

# Global lists to manage clients
clients = []
names = {}

# Handle individual client connections
def handle_client(client_socket):
    while True:
        # Request and validate chatname
        client_socket.send("Enter your chatname: ".encode())
        chatname = client_socket.recv(1024).decode()

        if chatname in names.values():
            client_socket.send("Name already taken. Please choose a different name.".encode())
        else:
            names[client_socket] = chatname
            break
    
    clients.append(client_socket)
    print(f"{chatname} joined the chat.")
    broadcast(f"{chatname} has joined the chat.", client_socket)

    # Listen for messages from this client
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message == '{quit}' or message == '{close}':
                client_socket.send("{quit}".encode())
                clients.remove(client_socket)
                broadcast(f"{chatname} has left the chat.", client_socket)
                del names[client_socket]
                client_socket.close()
                break
            else:
                handle_message(client_socket, chatname, message)
        except:
            clients.remove(client_socket)
            del names[client_socket]
            break

# Handle message and check for private messages
def handle_message(client_socket, chatname, message):
    if message.startswith('@'):
        parts = message.split(' ', 1)
        if len(parts) > 1:
            recipient_name = parts[0][1:]  # Get the recipient's name
            private_message(chatname, recipient_name, parts[1])
        else:
            client_socket.send("Usage: @username message".encode())
    else:
        broadcast(f"{chatname}: {message}", client_socket)

# Send private messages to a specific user
def private_message(sender_name, recipient_name, message):
    for client, name in names.items():
        if name == recipient_name:
            client.send(f"Private from {sender_name}: {message}".encode())
            break
    else:
        # If the recipient does not exist
        for client in clients:
            client.send(f"User  {recipient_name} not found.".encode())

# Broadcast messages to all clients
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            client.send(message.encode())

# Main server function
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print("Server started and waiting for clients...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} established.")
        
        # Start thread for client
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

start_server()