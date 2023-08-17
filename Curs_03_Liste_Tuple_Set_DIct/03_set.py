# SET ( Setul ) - { valoare1, valoare2, .... }
'''         PROPRIETATI SET
- setul este o colectie de elemente UNICE ( nu poti avea valori duplicat ) ! - UNICITATE
- elementele pot fi de tipuri diferite
- NU este ordonat, NU ARE INDEX
- este MUTABILA ( adaugam, stergem, atat ) - nu putem modifica elemente
- fiecare element din set trebuie sa fie IMUTABIL !
- valorile setului fiind unice sunt considerate ca chei ( keys )
- un set gol se defineste : set()
'''

# cream un set :
data_curenta = {2023, 'iulie', 11, True, 19, 49, 'PM'}
print(f"data_curenta : {data_curenta}")

print('--' * 30)

# Adaugam o valoare:
data_curenta.add(2022)
print(f"data_curenta : {data_curenta}")

# Adaugam un tuple
data_curenta.add((7, 8, 9))
print(f"data_curenta : {data_curenta}")

print('--' * 30)

# Stergem un element existent :
data_curenta.remove(2022)
print(f"data_curenta : {data_curenta}")
# eroare in caz ca cheia nu exista

print('--' * 30)

# print lungime
print(f'lungime set data_curenta : {len(data_curenta)}')
