def poziomstresu(rodzaj_pracy, tiki_nerwowe):
    stres = 0
    if rodzaj_pracy == 2:
        stres += 1
    if rodzaj_pracy == 3:
        stres += 2
    if tiki_nerwowe:
        stres += 1
    return stres


def ileruchu(ile_zwyklego_ruchu, ile_cwiczen):
    ruch = 0
    if ile_zwyklego_ruchu > 7:
        ruch += 2
    elif ile_zwyklego_ruchu > 5:
        ruch += 1
    if ile_cwiczen > 7:
        ruch += 2
    elif ile_cwiczen > 5:
        ruch += 1
    return ruch


def jakadieta(czy_wege, czy_tlusto):
    dieta = 0
    if czy_wege:
        dieta += 3
    if czy_tlusto:
        dieta -= 2
    return dieta
