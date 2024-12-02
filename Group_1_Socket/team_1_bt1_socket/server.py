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
                broadcast(f"{chatname}: {message}", client_socket)
        except:
            clients.remove(client_socket)
            del names[client_socket]
            break

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
