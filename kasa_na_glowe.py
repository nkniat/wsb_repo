zarobki_mama = float(input('Ile zarabia mama? '))
zarobki_tata = float(input('Ile zarabia tata? '))
ilosc_dzieci = int(input('Ile posiadacie dzieci? '))
ilosc_czlonkow_rodziny = int(input('Ile osób w rodzinie? '))
czy_kredyt = input('Czy rodzina posiada kredyt?  T/N ')
if czy_kredyt == 'T':
    kredyt = float(input('Jaka jest mieieczna rata kredytu? '))
kasa_na_glowe = (zarobki_mama + zarobki_tata + ilosc_dzieci * 500 - kredyt) / ilosc_czlonkow_rodziny
print('W rodzinie przypada ', kasa_na_glowe, ' na głowę')
if kasa_na_glowe < 600:
    kasa_na_glowe = kasa_na_glowe + 200
    print('Przyznaję socjal 200zł')
    print('W rodzinie przypada teraz ', kasa_na_glowe, ' na głowę')
