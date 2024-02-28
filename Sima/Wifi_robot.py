import socket
import time 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 8090))
s.listen(0)                 
 
client, addr = s.accept()
client.send(b'START')