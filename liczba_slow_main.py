from liczba_slow_funkcje import *

path = 'C://Users//kniat//PycharmProjects//wsb_git//wsb_repo//rolling_stones.txt'

text = zapisDanychzPliku(path)
text = przygotowanie(text)

print('liczba unikalnych słów to ', ileSlow(text), '\n')

print(ileRazy(text))
