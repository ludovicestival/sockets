"""Mirror server"""

import socket

final_mssg = 'fin'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('172.16.20.210', 63000))
server.listen(1)

conn, addr = server.accept()
print(f'Connected to {addr}')

while True:
    mssg = conn.recv(1024).decode()
    if mssg == final_mssg:
        break
    conn.send(mssg.encode())
