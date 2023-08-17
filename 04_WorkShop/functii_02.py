# 16
'''
16.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune.

Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Răspuns: {2, 3}

'''
def gaseste_numere_comune(lista1, lista2):
    set_lista1 = set(lista1)
    set_lista2 = set(lista2)
    numere_comune = set_lista1.intersection(set_lista2)
    return numere_comune
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
rezultat = gaseste_numere_comune(list1, list2)
print(rezultat)