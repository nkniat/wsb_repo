plec = input('Podaj plec K/M ')
wiek = int(input('Podaj wiek '))
aktywnosc = int(input('Jak aktywny jesteś w skali 0 - 10? '))

if wiek > 0 and wiek <= 18:
    print('Czesc')
    if plec == 'M' or plec == 'm':
        print('Chlopaku')
    elif plec == 'K' or plec == 'k':
        print('Dziewczyno')
    else:
        print('Plec nieznana')
    if aktywnosc >= 7:
        print('Chcesz pobiegać?')
elif wiek > 18 and wiek < 150:
    print('Dzien dobry')
    if plec == 'M' or plec == 'm':
        print('Szanowny Panie')
        if aktywnosc >= 7:
            print('Chce Pan pobiegać?')
    elif plec == 'K' or plec == 'k':
        print('Szanowna Pani')
        if aktywnosc >= 7:
            print('Chce Pani pobiegać?')
    else:
        print('Plec nieznana')
else:
    print('\nWiek się nie zgadza\n')
