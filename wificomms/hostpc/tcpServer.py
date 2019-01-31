import socket

print(socket.gethostname())
TCP_IP = socket.gethostbyname(socket.gethostname())
TCP_PORT = 80
BUFFERSIZE = 20
MESSAGE = "Hello World!"

print("Opening Socket")
# SOCK_STREAM refers to a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Binding Socket")
s.bind((TCP_IP, TCP_PORT))
print("Listening...")
s.listen(1)
print("Started listening on %s, port %d" %(TCP_IP, TCP_PORT))

conn, addr = s.accept()
print("Connection Address: %s" % addr)
while 1:
    data = conn.recv(BUFFERSIZE)
    if not data: break
    print("Received data: %s" % data)
    conn.send(data)  # echo
conn.close()
