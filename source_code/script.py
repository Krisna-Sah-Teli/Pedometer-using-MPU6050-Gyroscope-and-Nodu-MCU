import socket

server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 1234))
server_socket.listen(1)

print("Server started")

while True:
    conn, addr = server_socket.accept()
    print("New connection from ", addr)

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("Received: ", data)

    conn.close()
    print("Connection closed")