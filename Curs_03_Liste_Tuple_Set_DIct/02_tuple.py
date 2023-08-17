## TUPLE (valoare1, valoare2, .... )
'''
- tuple este un tip de date IMUTABIL ( NU SE POT sterge. adauga, modifica valori )
 - sunt valori ordonate, indexabile
 - pot exista mai multe valori repetate
'''

# Definim un tuple - ()
tuple_numere = (1, 2, 3)
print(f"tuple_numere : {tuple_numere}")

# nu se pot schimba valori => Imposibil
# tuple_numere[-1] = 4

print('--' * 30)

lista_litere = ["a", "b", "c", "a"]
print(f"lista_litere : {lista_litere}")
lista_litere.append("d")
print(f"lista_litere : {lista_litere}")

# Transform o lista intr-un tuple :
tuple_litere = tuple(lista_litere)
print(f"tuple_litere : {tuple_litere}")

print('--' * 30)

# Pot sa le numar si sa le accesez cu index
elem1 = tuple_litere[0]
print(f"elem1 : {elem1}")
print(f"verific lungime tuple : {len(elem1)}")

print(f"numar cate elemente sunt in tuple : {tuple_litere.count('a')}")

print('--' * 30)

# Exemplu de utilizare a tuple-lului
triunghi_dat = ((0, 0), (0, 3), (2, 4))
