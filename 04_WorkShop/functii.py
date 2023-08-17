# 1
import time


def calcul_suma(a, b):
    suma = a + b
    return suma


rezultat = calcul_suma(4, 10)
print(rezultat)
print("*" * 30)


# 2
def comparare_numere(a):
    if a % 2 == 0:
        return True
    else:
        return False


c = comparare_numere(5)
d = comparare_numere(4)
print(c)
print(d)

print("*" * 30)


# 3

def calcul_caractere(nume, prenume, nume_mijlociu):
    nume_complet = nume + prenume + nume_mijlociu
    numar_caractere = len(nume_complet)
    return numar_caractere


e = calcul_caractere("Adrian", "Holom", "Anderi")
print(e)

print("*" * 30)


# 4
def aria_dreptunghiului(lungime, inaltime):
    aria = lungime * inaltime
    return aria


rezultat = aria_dreptunghiului(10, 32)
print(rezultat)
print("*" * 30)


# 5
def arie_cerc(r):
    arie_c = 3.14 * r ** 2
    return arie_c


rezultat = arie_cerc(10)
print(rezultat)
print("*" * 30)
import math


def calcul_aria_cerc(raza):
    aria = math.pi * raza ** 2
    return aria


rezultat = calcul_aria_cerc(10)
print(rezultat)
print("*" * 30)


# 6
def gaseste_caracter(x, string):
    if x in string:
        return True
    else:
        return False


rezultat = gaseste_caracter("b", "abc")
print(rezultat)
rezultat = gaseste_caracter("b", "dfg")
print(rezultat)
print("*" * 30)


# 7
def numara_caractere(sir):
    lower = 0
    upper = 0
    for caracter in sir:
        if caracter.islower():
            lower += 1
        elif caracter.isupper():
            upper += 1
    print(f"Numar caractere lower este {lower}")
    print(f"Numar caractere upper este {upper}")


numara_caractere("Ala Bala PortocalA")
print("*" * 30)


# 8
def filtreaza_nr_pozitive(lista):
    '''
    Functia preia o lista de numere negative si pozitive si filtreaza numerele pozitive
    :param lista: lista cu numere
    :return: lista cu numere pozitive
    '''
    lista_pozitiva = []
    for n in lista:
        if n >= 0:
            lista_pozitiva.append(n)
    return lista_pozitiva


lista = [1, 2, 4, 0, -3, -5, 4, 8, -7]
rezultat = filtreaza_nr_pozitive(lista)
print(rezultat)
print("*" * 30)


# 9
def comparara_numere(x, y):
    if x > y:
        print(f"Primul numar {x} este mai mare decat al doilea numar {y}")
    elif y > x:
        print(f"Al doilea numar {y} este mai mare decat primul numar {x}")
    else:
        print(f"Numerele {x} si {y} sunt egale")


comparara_numere(4, 6)
comparara_numere(8, 4)
comparara_numere(6, 6)
print("*" * 30)


# 10
def adauga_numar_in_set(numar, set):
    if numar in set:
        print(f"Numarul {numar} exista deja")
        return False
    else:
        set.add(numar)
        print(f"Am adufgat numarul {numar} in set")
        return True


set = {1, 2, 3}
rezultat = adauga_numar_in_set(4, set)
rezultat = adauga_numar_in_set(3, set)
print("*" * 30)


# 11
def numar_zile_in_luna(luna):
    if luna == 2:
        return 28
    elif luna in [4, 6, 9, 11]:
        return 30
    else:
        return 31


numa_zile = numar_zile_in_luna(7)
print(numa_zile)
numa_zile = numar_zile_in_luna(4)
print(numa_zile)
numa_zile = numar_zile_in_luna(2)
print(numa_zile)
print("*" * 30)


# 12
def calculator(a, b):
    suma = a + b
    diferenta = a - b
    inmultirea = a * b
    impartirea = a / b
    return suma, diferenta, inmultirea, impartirea


a, b, c, d = calculator(10, 3)
print(f"Suma = {a}")
print(f"DIferenta = {b}")
print(f"Inmltirea = {c}")
print(f"Impartirea = {d}")

print("*" * 30)

'''
13. Funcție care primește o listă de cifre (adică doar 0-9) 
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0

'''

# def numara_aparitii_cifre(lista):
#     aparitii_cifra = {}  # initoalizare dictionar gol
#     for cifra in lista:  # parcurgem fiecare cifra din lista de intrare
#         if cifra not in aparitii_cifra:  # verifica daca cifra nu a fost in dictionar
#             aparitii_cifra(cifra) == 1  # daca cifra e intalnita prima data adauga 1
#         else:
#             aparitii_cifra(cifra)  += 1  #
#     for cifra in range(10):
#         aparitii_cifra(cifra) = 0
#     return aparitii_cifra
# lista = [1, 3, 1, 5, 9, 7, 7, 5, 5]
# rezultat = numara_aparitii_cifre(lista)
# print(rezultat)
print("*" * 30)

# 14
def gaseste_numere(a, b, c):
    return max(a, b, c)


rezultat = gaseste_numere(2, 4, 6)
print(rezultat)
print("*" * 30)

# 15
def calculeaza_suma_pana_la(numar):
    suma = 0
    for i in range(numar+1):
        suma += i
    return suma
rezultat = calculeaza_suma_pana_la(3)
print(rezultat)
print("*" * 30)
# 16
'''
16.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune.

Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Răspuns: {2, 3}

'''
# def gaseste_numere_comune(lista1, lista2):
#     set_lista1 = set(lista1)
#     set_lista2 = set(lista2)
#     numere_comune = set_lista1.intersection(set_lista2)
#     return numere_comune
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# rezultat = gaseste_numere_comune(list1, list2)
# print(rezultat)
# 17
'''
17. Funcție care să aplice o reducere de preț.
Dacă produsul costă 100 lei și aplicăm reducere de 10%. Pretul va fi 90 de lei.
Tratează cazurile în care reducerea e invalidă. De exemplu o reducere de 110% e invalidă.


'''
# def aplica_reducere(pret, reducere):
#     if reducere < 0 or reducere > 100:
#         print("Reducerea este invalida")
#         return None
#     else:
#         pret_produs = pret * (1-reducere/100)
#         return pret_produs
# pret_inital = 100
# reducere = 10
# pret_redus = aplica_reducere(pret_inital, reducere)
# print(pret_redus)
# if pret_redus is not None:
#     print()

# 18
import datetime
import pytz
def afisaja_data_ora():
    fus_ora_ro = pytz.timezone("Europe/Bucharest")
    data_ora_ro = datetime.datetime.now(fus_ora_ro)
    print(f"Data si ora in Romania este {data_ora_ro}")

    fus_ora_cn = pytz.timezone("Asia/Shanghai")
    data_ora_cn = datetime.datetime.now(fus_ora_cn)
    print(f"Data si ora in China este {data_ora_cn}")
afisaja_data_ora()
for i in range(10):
    afisaja_data_ora()
    time.sleep(1)

