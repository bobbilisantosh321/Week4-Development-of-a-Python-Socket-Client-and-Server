import socket

s = socket.socket()

port = 9500

s.connect(('127.0.0.1', port))

print("Client sent How are you")
s.send(b'How are you?')
print("Client Received ")
print(s.recv(1024))

s.close()

s = socket.socket()

s.connect(('127.0.0.1', port))

print("Client sent Hello")
s.send(b'Hello')
print("Client Received ")
print(s.recv(1024))

s.close()
