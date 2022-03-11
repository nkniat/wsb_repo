import os
import time

print(os.getcwd())                           #wypisanie aktualnej lokalizacji
os.chdir('C:\\Users\\kamil\\Desktop')     #zmiana lokalizacji
print(os.getcwd())                           #wypisanie aktualnej (nowej) lokalizacji
os.mkdir('new_folder')                       #utworzenie folderu
time.sleep(5)                                #czekanie 5 sekund
os.rename('new_folder', 'new_folder2')       #zmiana nazwy folderu
time.sleep(5)                                #czekanie 5 sekund
os.rmdir('new_folder2')                      #usunięcie folderu

#przejście na pulpit i wyszukanie rekursywne pliku new.txt. Wynik zwrócony do pliku result.txt
os.system('cmd /c "cd C://Users//kamil//Desktop && dir /s new.txt >> result.txt"')
