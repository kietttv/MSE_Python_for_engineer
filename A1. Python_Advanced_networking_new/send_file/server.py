# server_file.py

import socket

# host = socket.gethostname() # or host = "localhost"
host = 'localhost'
# Specify the port to listen on
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
print("Server listening on port", port)

c, addr = s.accept()

# Receive the file name from the client
filename = c.recv(1024).decode()

try:
    with open(filename, 'rb') as f:
        content = f.read()
    # Send the file content to the client
    c.send(content)
except FileNotFoundError:
    # Send error message if file not found
    c.send(b"File not found")

c.close()
s.close()
