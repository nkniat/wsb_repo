import os
import datetime
import time

now = datetime.datetime.now()
timer = now.strftime('%H_%M_%S')

path = 'C://Users//kamil//Desktop//' + timer + 'tmp.txt'
command = 'tracert 8.8.8.8 >> ' + path
print(os.getcwd())
os.chdir('C://Users//kamil//Desktop')
print(os.getcwd())

#os.system('cmd /c "tracert 8.8.8.8 > C:/Users/kamusial/Desktop/new.txt"')
#os.system(f'cmd /c {command}')

ts1 = time.time()         #timestamp ts1
os.system(f'cmd /c "tracert 8.8.8.8 >> {path}"')
ts2 = time.time()         #timestamp ts1

print(f'Tracert command took {round(ts2-ts1)} seconds')

with open(path, 'r') as tracert:       #odczytanie pliku
    content = tracert.readlines()
#print(content)

#odczytanie ilości hopków oraz czasu
star_counter = 0
for i in range (len(content)):
    content[i] = content[i].split()
    if len(content[i]) > 1 and content[i][1] == '*':
        star_counter += 1
print(content)
no_of_hops = int(content[-3][0]) - star_counter

time_to_get = 0
for i in range (4, (len(content)-2)):
    content[i][1] = content[i][1].replace(' ', '')
    content[i][1] = content[i][1].replace('ms', '0')
    content[i][1] = content[i][1].replace('*', '0')
    time_to_get += int(content[i][1])
print()
print(f'Hoop number to 8.8.8.8 is {no_of_hops} and total time is {time_to_get} ms ')
