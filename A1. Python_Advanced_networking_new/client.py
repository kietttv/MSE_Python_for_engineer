import socket

# ipServer = "10.26.16.203"
# portServer = 8080
ipServer = input("Nhap ip: ")
portServer = int(input("Nhap port: "))


# Create a socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect((ipServer, portServer))

msg = clientSocket.recv(1024)

while msg:
    print(f"Msg = {msg.decode()}")
    msg = clientSocket.recv(1024)