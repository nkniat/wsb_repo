#zakładamy, że pasel ma 4 cyfry
def sprawdzpesel(pesel):
    if pesel > 999 and pesel < 10000:
        return True
    else:
        return False


ilosc_osob = int(input('Ile jest osob? '))
tablica_osoby = []
tablica_wszystkich_osob = []
tablica_nazwiska = []
slownik_nazwisk = {}
#w tablicy wszystkich osób będą mniejsze tablice - jedna dla każdej osoby
#tablica dla każdej osoby będzie zawierała kolejno: imię, nazwisko, wiek, PESEL

for i in range (ilosc_osob):
    print('Wpisuję dane ', i+1, ' osoby ')
    imie = input('Podaj imię ')
    tablica_osoby.append(imie)
    nazwisko = input('Podaj nazwisko ')
    tablica_osoby.append(nazwisko)
    tablica_nazwiska.append(nazwisko)
    wiek = int(input('Podaj wiek '))
    tablica_osoby.append(wiek)
    while True:
        pesel = int(input('Podaj PESEL '))
        print('Sprawdzam PESEL')
        if sprawdzpesel(pesel):
            tablica_osoby.append(pesel)
            break
        else:
            print('Zly PESEL - za dlugi albo za krotki')
            print('Jeszcze raz')
    tablica_wszystkich_osob.append(tablica_osoby)
    print('Wpisano osobę ', tablica_osoby)
    tablica_osoby = []

#zapisujemy nazwiska w slowniku, sprawdzamy powtorzenia
for i in tablica_nazwiska:
    if i in slownik_nazwisk:
        slownik_nazwisk[i] += 1
    else:
        slownik_nazwisk[i] = 1

#wypisujemy powtarzające się nazwiska
for a, b in slownik_nazwisk.items():
    if b > 1:
        print(f'Nazwisko {a} powtarza się {b} razy ')

#sredni wiek
wiek_suma = 0
sredni_wiek = 0
for i in tablica_wszystkich_osob:
    wiek_suma += i[2]
sredni_wiek = wiek_suma / len(tablica_wszystkich_osob)
print('Sredni wiek to: ', round(sredni_wiek, 2))
