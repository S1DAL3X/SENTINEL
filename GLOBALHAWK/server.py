import socket, sys

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5003

BUFFER_SIZE = 4096

s = socket.socket()

s.bind((SERVER_HOST, SERVER_PORT))
#делаем порт многоразовым
#настройки соединения
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.listen(5)
print('\nGLOBALHAWK is started!')
print(f'Listening as {SERVER_HOST} : {SERVER_PORT} ...')

client_socket, client_address = s.accept()
print(f'{client_address[0]} : {client_address[1]} was connected!')

message = 'GLOBALHAWK is connected!'.encode()
client_socket.send(message)

while True:
    command = input('\nGLOBALHAWK > ')
    client_socket.send(command.encode())

    if command.lower() == 'exit':
        break

    results = client_socket.recv(BUFFER_SIZE).decode()
    print(results)

client_socket.close()
s.close()
