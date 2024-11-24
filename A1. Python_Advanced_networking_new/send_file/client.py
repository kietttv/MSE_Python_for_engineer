# client_file.py

import socket

s = socket.socket()
s.connect(("localhost", 8080))  # Connect to server on port 8080

# Enter the file name
filename = input("Enter a filename: ")

# Send the file name to the server
s.send(filename.encode())

# Receive the file content or error message from the server and display it
content = s.recv(1024)
print(content.decode())

s.close()
