import pandas as pd

path = 'C://Users//kamil//Desktop//Uczelnie//aWSB//1_zimowy21_22//Podyplomowe//Chorzów - 16h + 8h//2. zdalne Katowice 12.02.2022//1. Python dev//pliki//pokemon.csv'

data = pd.read_csv(path, delimiter=',')
print(data.head(4))
print(data.columns)
print(data[['Name', 'Type 1', 'HP']][0:5])
print(data.iloc[1:4])
print (data.iloc[2,1])

for index, row in data.iterrows():
    print(index, row[['Name','Type 1']])

print (data.loc[data['Type 1'] == 'Fire'])

print(data.describe())

# print(data.sort_values('Name', ascending=False))
# print(data.sort_values(['Type 1','Speed']))
#print(data.sort_values(['Type 1','Speed'], ascending=False))
# najpierw Type 1, dalej HP
#print(data.sort_values(['Type 1','Speed'], ascending=[1,0]))
#Type 1 - ascending,  Speed descending

#making changes to the data

# print(data.head(5))
# data['Total'] = data['HP'] + data['Attack'] + data['Defense']
# print(data.head(5))
# data = data.drop(columns=['Total'])
# print(data.head(5))

# print(data.iloc[3])
# data['Total'] = data.iloc[:, 4:10].sum(axis=1)
# cols = list(data.columns)
# data = data[cols[0:4] + [cols[-1]] + cols[4:12]]
# print(data.iloc[3])
# #dodanie kolumny i zamiana kolumn
#
# data.to_csv('C:\\Users\\kamil\\Desktop\\modified_pokemon.csv', index=False, sep=';')
# data.to_excel('C:\\Users\\kamil\\Desktop\\modified_pokemon.xlsx', index=False)
# data.to_csv('C:\\Users\\kamil\\Desktop\\modified_pokemon.txt', index=False, sep='\t')
