import socket
import os

os.chdir('C://Users//kamil//Desktop')
os.system(f'cmd /c "ipconfig /all > ip.txt"')    #zapisanie w pliku ip.txt informacji

with open('C://Users//kamil//Desktop//ip.txt', 'r', encoding='ANSI') as ip_file:
    content = ip_file.readlines()
print(content)

for i in content:
    if 'Host Name' in i:
        host_name = i[39:-1]
print(f'\nHost Name odczytany z pliku to: {host_name}')

for i in content:
    if '(Preferred)' in i:
        ip_address = i[39:-13]
print(f'Adress IP odczytany z pliku to: {ip_address}\n')

#2ga metoda z użyciem biblioteki socket
hostname = socket.gethostname()               #zapis nazwy hosta
local_ip = socket.gethostbyname(hostname)     #zapis adresu IP
print(f'Hostname otrzymany dzięki bibliotece "socket" to: {hostname}')
print(f'Adres IP otrzymany dzięki bibliotece "socket" to: {local_ip}')
