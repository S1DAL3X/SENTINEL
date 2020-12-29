import time, subprocess
from bs4 import BeautifulSoup  
from urllib.request import urlopen 

print('\nBEEZYFREE is started...\n')
time.sleep(2)
print("#" * 30)
print('\n')
time.sleep(2)

#Out IP
def get_outside_ip():
    url = urlopen('https://yandex.ru/internet/')   
    soup = BeautifulSoup(url, 'html.parser')
    out_str = soup.find('li', class_='parameter-wrapper general-info__parameter')
    out_str = str(out_str)                                                      
    ip = []
    
    for symbol in out_str:
        if '1234567890.'.find(symbol) != -1:
            ip.append(symbol)
    OUTSIDE_IP = ''.join(ip)[3:]
    return(OUTSIDE_IP)

try:
    print('IP : ' + str(get_outside_ip()))
    get_outside_ip()
    with open('log.txt', 'a') as f:
        f.write('IP : ' + str(get_outside_ip()) + '\n')
        f.write('#' * 200)
        f.close()
        
except:
    print('Не удалось определить IP')

#ipconfig /all
try:
    reply = subprocess.check_output(['ipconfig', '/all'], stderr = subprocess.PIPE)
    
    with open('log.txt', 'a') as f:
        f.write(reply.decode('CP866'))
        f.write('#' * 200)
        f.close()
        
    print('Command 1 is Success!')
except:
    print('Command 1 is Error!')

#netstat -ano
try:
    reply = subprocess.check_output(['netstat', '-ano'], stderr = subprocess.PIPE)
    
    with open('log.txt', 'a') as f:
        f.write(reply.decode('CP866'))
        f.write('#' * 200)
        f.close()
        
    print('Command 2 is Success!')
except:
    print('Command 2 is Error!')

#net start
try:
    reply = subprocess.check_output(['net', 'start'], stderr = subprocess.PIPE)
    
    with open('log.txt', 'a') as f:
        f.write(reply.decode('CP866'))
        f.write('#' * 200)
        f.close()
        
    print('Command 3 is Success!')
except:
    print('Command 3 is Error!')

#tasklist /v
try:
    reply = subprocess.check_output(['tasklist', '/v'], stderr = subprocess.PIPE)
    
    with open('log.txt', 'a') as f:
        f.write(reply.decode('CP866'))
        f.write('#' * 200)
        f.close()
        
    print('Command 4 is Success!')
except:
    print('Command 4 is Error!')

#net user
try:
    reply = subprocess.check_output(['net', 'user'], stderr = subprocess.PIPE)
    
    with open('log.txt', 'a') as f:
        f.write(reply.decode('CP866'))
        f.write('#' * 200)
        f.close()
        
    print('Command 5 is Success!')
except:
    print('Command 5 is Error!') 

