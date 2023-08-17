# DICT - DICTIONARUL    -   {
#         cheie1 : valoare1
#         cheia2 : valoare2
#         .... : ....
#         }
'''
- dictionarul este o colectie de date de tip cheie-valoare ( fiecare cheie are o valoare )
- dictionarul in sine este MUTABIL
- cheile ( keys ) sunt unice !
- valorile (values) se pot repeta
- cheile trebuie sa fie IMMUTABLE ( doar de tip : int, str, tuple )
'''

# Initializare dictionar
persoana = {
    'nume': 'Stefan',
    'prenume': 'Gheorghiu',
    'varsta': 47
}

print(f'persoana = {persoana}')

# Adaugarea unui element in dictionar
persoana['initiala_tatalui'] = 'P'
print(f"persoana = {persoana}")

# Modificarea unui element existent ( folosesc cheia pe care o doresc )
persoana['initiala_tatalui'] = 'Y'
print(f"persoana = {persoana}")

# Stergere elemente :
persoana.pop('initiala_tatalui')
print(f"persoana = {persoana}")

print('--' * 30)

# accesarea unui element existent / non-existent => eroare ( ca si la set )
print(f"valoarea cheii unui elem : {persoana['varsta']}")
# print(f"valoarea unui elem : {persoana['var']}")        # KeyError: 'var'

print('--' * 30)

# lungimea dictionarului
lungime_dict = len(persoana)
print(f"lungime dict = {lungime_dict}")

print('--' * 30)