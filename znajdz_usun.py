import os

#pierwsza metoda.... znaleźć pliki, wyciągnąć ścieżki i skasować. Nieskończone - bez sensu ;)
# os.system('cmd /c "cd C://Users//kamil//Desktop && dir /s *.pcap >> result.txt"')
#
# with open ('C://Users//kamil//Desktop//result.txt', 'r', encoding='ANSI') as search_pcap:
#     content = search_pcap.readlines()

#2ga metoda - komenda del /S *.pcap w terminalu
os.system('cmd /c "cd C://Users//kamil//Desktop && del /S *.pcap"')
