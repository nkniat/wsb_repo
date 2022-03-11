def zapisDanychzPliku(path):
    with open(path, 'r') as plik:
        content = plik.read()
    content = content.split()
    print(f'Otwarto plik {path}\n')
    return content


def przygotowanie(text):
    print('Rozpoczeto przygotowanie pliku')
    print('zamiana wszystkiego na male litery')
    print('usuniecie kropek')
    for i in range(len(text)):
        text[i] = text[i].lower()
        text[i] = text[i].replace('.','')
    print('koniec przygotowan \n')
    return text


def ileRazy(text):
    print('Liczymy powtorzenia')
    slownik = {}
    for j in text:
        if j in slownik:
            slownik[j] += 1
        else:
            slownik[j] = 1
    # for a, b in slownik.items():
    #      print(f'slowo {a} powtarza się {b} razy')
    max_key = max(slownik, key=slownik.get)
    all_values = slownik.values()
    max_value = max(all_values)
    print(f'slowo "{max_key}" powtarza się {max_value} razy\n')


def ileSlow(text):
    tekst = set(text)
    return len(set(text))
