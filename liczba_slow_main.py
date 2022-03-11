from plik_def import *

path = 'C://Users//kamusial//Desktop//rolling_stones.txt'

text = zapisDanychzPliku(path)
text = przygotowanie(text)

print('liczba unikalnych słów to ', ileSlow(text), '\n')

print(ileRazy(text))
