#zakładamy, że pasel ma 4 cyfry
def sprawdzpesel(pesel):
    if pesel > 999 and pesel < 10000:
        return True
    else:
        return False


def wpiszosobe():
    print('Wpisuję dane ', i + 1, ' osoby ')
    imie = input('Podaj imię ')
    tablica_osoby.append(imie)
    nazwisko = input('Podaj nazwisko ')
    tablica_osoby.append(nazwisko)
    tablica_nazwiska.append(nazwisko)
    wiek = int(input('Podaj wiek '))
    tablica_osoby.append(wiek)


def wprowadzpesel():
    while True:
        pesel = int(input('Podaj PESEL '))
        print('Sprawdzam PESEL')
        if sprawdzpesel(pesel):
            tablica_osoby.append(pesel)
            break
        else:
            print('Zly PESEL - za dlugi albo za krotki')
            print('Jeszcze raz')


def sredniwiek():
    wiek_suma = 0
    sredni_wiek = 0
    for i in tablica_wszystkich_osob:
        wiek_suma += i[2]
    sredni_wiek = wiek_suma / len(tablica_wszystkich_osob)
    return sredni_wiek


ilosc_osob = int(input('Ile jest osob? '))
tablica_osoby = []
tablica_wszystkich_osob = []

#w tablicy wszystkich osób będą mniejsze tablice - jedna dla każdej osoby
#tablica dla każdej osoby będzie zawierała kolejno: imię, nazwisko, wiek, PESEL

for i in range (ilosc_osob):
    wpiszosobe()
    wprowadzpesel()
    tablica_wszystkich_osob.append(tablica_osoby)
    print('Wpisano osobę ', tablica_osoby)
    tablica_osoby = []


#sredni wiek
sredni_wiek = sredniwiek()
print('Sredni wiek to: ', round(sredni_wiek, 2))
