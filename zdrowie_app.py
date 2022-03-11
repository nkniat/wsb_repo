# program liczy prawdopodobnieństwo, że pacjent będzie miał problemy z sercem
# program bierze pod uwagę stres, ruch i dietę
from funkcje import *

rodzaj_pracy = int(input('Jaki masz rodzaj pracy?\n1.Zwykla\n2.zarządzanie\n3.Wysokiego ryzyka\n'))
tiki = input('Czy masz tiki nerwowe?  T/N   ')
if tiki == "T" or tiki == "t" or tiki == "Tak":
    tiki = True
else:
    tiki = False
stres = poziomstresu(rodzaj_pracy, tiki)

zwykly_ruch = int(input('Ile masz zwyklego ruchu?  1-10  '))
ile_cwiczen = int(input('Ile masz cwiczen?  1-10  '))
ruch = ileruchu(zwykly_ruch, ile_cwiczen)

wege = input('czy jestes wege?  T/N  ')
if wege == "T":
    wege = True
else:
    wege = False
tlusto = input('czy jesz tlusto?  T/N  ')
if tlusto == "T":
    tlusto = True
else:
    tlusto = False
dieta = jakadieta(wege, tlusto)

wynik = ruch + dieta - stres
if wynik > 2:
    print('Dobre zdrowie')
elif wynik > 0:
    print('srednie zdrowie')
else:
    print('slabo')