import socket

SERVER = input('IP to connect to: ')
PORT = int(input('Port: '))

print('Setting up socket...')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f'Connecting to {SERVER}:{PORT}...')
sock.connect((SERVER, PORT))
print('Connected to Server. Awaiting message...')

while True:
    try:
        message = sock.recv(1024).decode()
        print(message)
        sock.close()
    except:
        break
