import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFERSIZE = 20
MESSAGE = "Hello World!"

# SOCK_STREAM refers to a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print("Connection Address: %s" % addr)
while 1:
    data = conn.recv(BUFFERSIZE)
    if not data: break
    print("Received data: %s" % data)
    conn.send(data)  # echo
conn.close()
