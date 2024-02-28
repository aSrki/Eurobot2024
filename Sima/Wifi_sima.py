import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '192.168.77.219'
server_address = (server_ip, 8090)

client_socket.connect(server_address)

# Receive message from server
receive = client_socket.recv(1024)
print("Received from server:", receive.decode())

client_socket.close()
