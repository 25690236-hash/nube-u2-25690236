import socket 
c = socket.socket()
c.connect(("localhost",5001))
c.send(b"hola")
print(c.recv(1024))
