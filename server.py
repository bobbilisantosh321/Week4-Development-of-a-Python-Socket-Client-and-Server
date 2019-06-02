import socket

s = socket.socket()
print("Socket successfully created")

port = 9500

s.bind(('', port))
print("socket binded to %s" % (port))

s.listen(5)
print("socket is listening")

while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    data = c.recv(1024)
    print(data)
    request = data.decode("utf-8")
    print("Server received ", request)
    if request == "Hello":
        print("Server is sending Hi")
        c.send(b'Hi')
    else:
        print("Server is sending Goodbye")
        c.send(b'Goodbye')
    c.close()