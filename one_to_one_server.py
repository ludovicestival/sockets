"""One-to-one server"""

import socket

final_mssg = 'fin'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 63000))
server.listen(1)

conn, addr = server.accept()
print(f'Connected to {addr}')

while True:
    mssg = conn.recv(1024).decode()
    print(f'Received: {mssg}')

    if mssg == final_mssg:
        break

    response = input('Send a response >')
    conn.send(response.encode())

    if response == final_mssg:
        break
