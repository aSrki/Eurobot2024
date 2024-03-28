import socket

# Receiver's IP and Port
host = '0.0.0.0'         # Listen on all available interfaces
port = 12345            # Same port as the sender

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
s.bind((host, port))

# Listen for incoming connections
s.listen(1)

# Accept a connection
conn, addr = s.accept()

# Receive data
data = conn.recv(1024).decode()
print('Received:', data)

# Close the connection
conn.close()
