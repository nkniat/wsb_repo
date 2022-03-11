#1. Odczyt pliku csv z zapisem poszczegolnych pol

path = 'C://Users//kamil//Desktop//rozliczenie.csv'
mode = 'r'
with open (path, mode) as plik2:
    content = plik2.readlines()                     #zapisujemy plik z podziałem na linię
for i in range (len(content)):
    content[i] = content[i].split(';')              #dzielimy linie na listy względem średników
print('Koniec czesci 1\n')

#2. Obliczenie sredniej wyplaty
total = 0                                              #deklarujemy zmienną
for i in range (1,len(content)):                       #pętla - dla każdej linii, prócz pierwszej
    total += int(content[i][1])                        #sumujemy wypłaty
average = total / (len(content)-1)                     #średnia to total dzielone przez liczbę pracowników
print('Średnia wyplata wynosi :', round(average,2))    #średnia zaokrąglona do 2 miejsc po przecinku
print('Koniec czesci 2\n')

#3. Obliczenie liczby kobiet na macierzynskim
total = 0                                              #deklarujemy zmienną
for i in range (1,len(content)):
    content[i][4] = content[i][4].replace('\n','')
    if content[i][3] == 'k' and content[i][4] == 't':
        total +=1
print('Liczba kobiet na macierzynskim wynosi ', total)
print('Koniec czesci 3\n')
