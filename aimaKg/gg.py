import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 8000))
sock.send(b'test message')
result = sock.recv(1024)
print(result.decode('utf-8'))
sock.close()

