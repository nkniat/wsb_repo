a = 'mama'
b = 'tata'
c = a+b    #łączenie stringów
print (c)

list_of_ids = ['123123','3453','6666','11111','34542','3445545']

for i in list_of_ids:
    name = 'Invoice for employee id='+i+'.'   #łączenie stringów w pętli
    print (name)
print()
print('ID is ', list_of_ids[3], ' or ', list_of_ids[4])    #zwykly print
print(f'ID is {list_of_ids[3]} or {list_of_ids[4]}')       #print z użyciem formatowania
