"""mini protocol server"""

# /commande args

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 63000))
server.listen(1)

conn, addr = server.accept()
print(f'Connected to {addr}')

try:
    while True:
        mssg = conn.recv(1024).decode()

        parts = mssg.split(' ', 1)
        cmd = parts[0]
        args = parts[1] if len(parts) > 1 else ''

        if cmd == "/bye":
            conn.send('fin'.encode())
            server.close()
            break
        elif cmd == '/up':
            conn.send(args.upper().encode())
except KeyboardInterrupt:
    pass
