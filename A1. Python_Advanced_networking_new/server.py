import socket

# Create a socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define IP and Port
ip = "10.26.16.203"
port = 8080

# Bind the socket to the address
serverSocket.bind((ip, port))

# Start listening for connections
serverSocket.listen(10)

print("Server started.....")

while True:
    # Accept an incoming connection
    clientSocket, addr = serverSocket.accept()
    print(f"Connection established with {addr}")
    
    # Send a message to the client
    clientSocket.send("Chao client".encode())
    
    # Close the client socket
    clientSocket.close()
