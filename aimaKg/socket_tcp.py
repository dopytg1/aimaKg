import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8000))
server_socket.listen()


while True:
    try:
        client, addrs = server_socket.accept()
    except KeyboardInterrupt:
        server_socket.close()
        break
    else:
        result = client.recv(1024)
        client.sendall(("HTTP/1.1 200 OK\n\n", 200))
        client.close()
        print("message: " + result.decode('utf-8'))
