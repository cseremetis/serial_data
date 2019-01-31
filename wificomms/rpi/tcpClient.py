import socket

TCP_IP = '192.168.1.19'
TCP_PORT = 80
BUFFERSIZE = 4096
MESSAGE = "Hello World!"
REQUEST = "GET /HTTP/1.1\nHost: google.com\r\n\r\n"


# SOCK_STREAM refers to a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connecting")

#"""
# Custom Connect
print("Connected. Sending Request")
s.send(MESSAGE.encode())
print("Request Sent")
data = s.recv(BUFFERSIZE)
print(data)
s.close()
#"""

"""
# Test Connect with Google
googleip = socket.gethostbyname("www.google.com")
print("googleip: %s" % googleip)
s.connect((googleip, TCP_PORT))
print("Connected to Google")
s.send(REQUEST.encode())
data = s.recv(BUFFERSIZE)
print(data)
s.close()
"""

print("Received data: %s" % data)
