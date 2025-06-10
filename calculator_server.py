"""Calculator server"""

import socket

final_mssg = 'fin'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 63000))
server.listen(1)

conn, addr = server.accept()
print(f'Connected to {addr}')

while True:
    mssg = conn.recv(1024).decode()

    if mssg == final_mssg:
        break

    try:
        print(f'Received: {mssg}')
        result = eval(mssg)
        conn.send(str(result).encode())
    except Exception as e:
        conn.send(f'Erreur: {e}'.encode())
    
