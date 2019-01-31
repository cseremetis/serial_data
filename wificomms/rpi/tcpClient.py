import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFERSIZE = 1024
MESSAGE = "Hello World!"

# SOCK_STREAM refers to a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFERSIZE)
s.close()

print("Received data: %s" % data)
