"""Multi-clients server"""

import socket

final_mssg = 'fin'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 172.16.20.210
server.bind(('127.0.0.1', 63000))
server.listen(1)


while True:
    conn, addr = server.accept()
    print(f'Connected to {addr}')

    while True:
        mssg = conn.recv(1024).decode()
        if mssg == final_mssg:
            break
        conn.send(mssg.encode())
    conn.close()
