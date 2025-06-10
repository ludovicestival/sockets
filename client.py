"""Interactive client"""

import socket

server = input('Connect to: ')

# Message to close the connection
final_mssg = 'fin'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server, 63000))

print(f'Type a message then press enter to send it. Enter "{final_mssg}" to close the connection.')
while True:
    mssg = input('> ')
    client.send(mssg.encode())
    response = client.recv(1024).decode()

    if response == final_mssg:
        break

    print(f'Server response: {response}')

