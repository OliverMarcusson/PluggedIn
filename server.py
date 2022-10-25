import socket
from threading import Thread

HOST = ''
PORT = 5555

print('Creating socket...')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f'Binding socket to *:{PORT}')
sock.bind((HOST, PORT))

print(f'Socket listening to port {PORT}')
sock.listen()

while True:
    print('Waiting for new client...')
    conn, addr = sock.accept()
    print(f'[!] {addr} Connected.')
    
    message = input('Message to send: ')
    send = input('Send message? (y/n): ')
    if send == "y":
        conn.send(message.encode())
        print(f'Closing connection to {addr}...')
        conn.close()
