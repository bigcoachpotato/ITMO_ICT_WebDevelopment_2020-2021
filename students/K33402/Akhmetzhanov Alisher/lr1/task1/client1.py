import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9090))
sock.send(b'Hello, server! \n')

data = sock.recv(1024)

print(data)

sock.close()


