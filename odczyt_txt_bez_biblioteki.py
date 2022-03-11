#1. Odczyt pliku

path = 'C://Users//kamil//Desktop//my_file.txt'
mode = 'r'
with open (path, mode) as plik1:
#    content1 = plik1.read()       #odczyt całego pliku, jako string
    content2 = plik1.read(5)      #odczyt pierwszych 5ciu znaków
    content3 = plik1.read(5)      #odczyt kolejnych 5 znaków
    content4 = plik1.readline()   #odczyt pierwszej linii
    content5 = plik1.readline()   #odczyt kolejnej linii
    content6 = plik1.readlines()  #odczyt reszty pliku, jako tablicy
#powyższe linie operują na pliku "plik1", dlatego posiadają wcięcie

#poniższe linie nie operują na pliku, dlatego nie ma wcięcia
#print(content1)
print(content2)
print(content3)
print(content4)
print(content5)

#powyższy program odczyta i wypisze jedynie "content1". Po odczytaniu całego pliku (content1)
#kolejne metody chcą czytać kolejną treść, której nie ma
#problem rozwiażemy komentująć linię 6 i 15.
print('Koniec czesci 2\n')

#2. Zapis pliku do odpowidniej postach
#2a. Cały plik jako string
with open (path, mode) as plik1:
    content = plik1.read()      #zapis pliku, jako string
print(content)
content = content.split()       #dzielimy "content" na listę - oddzielamy elementy spacjami
print(content)
print('Koniec czesci 2a\n')

#2b. Z podziałem na poszczególne linie
with open (path, mode) as plik1:
    content = plik1.readlines()    #zapis pliku, jako lista
print(content)
for i in range (len(content)):
    content[i] = content[i].split()       #dzielimy każdą linię na listę - oddzielamy elementy spacjami
print(content)
print('Koniec czesci 2b\n')
