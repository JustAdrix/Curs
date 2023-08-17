"""
1.Funcție care să calculeze și să returneze suma a două numere
"""
def calcul_suma(a, b):
    suma = a + b
    return suma

rezultat = calcul_suma(4, 2)
print(rezultat)

"""
2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar
"""
def numar_par(numar):
    if numar % 2 == 0:
        return True
    else:
        return False

rezultat = numar_par(4)
print(rezultat)
rezultat = numar_par(9)
print(rezultat)

"""
3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
"""
def calcul_caractere(nume, prenume, nume_mijlociu):
    nume_complet = nume + prenume + nume_mijlociu
    numar_caractere = len(nume_complet)
    return numar_caractere

rezultat = calcul_caractere("Mos", "Ion", "Roata")
print(rezultat)

"""
4. Funcție care returnează aria dreptunghiului
"""
def calcul_arie(lunigme, latime):
    aria = lunigme * latime
    return aria

rezultat = calcul_arie(4, 2)
print(rezultat)

"""
5. Funcție care returnează aria cercului
"""

import math
def calcul_aria_cerc(raza):
    aria = math.pi * raza**2
    return aria

rezultat = calcul_aria_cerc(1.8)
print(rezultat)

"""
6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și 
False dacă nu găsește.
"""

def gaseste_caracter(x, string):
    if x in string:
        return True
    else:
        return False

rezultat = gaseste_caracter("b", "abc")
print(rezultat)
rezultat = gaseste_caracter("d", "abc")
print(rezultat)

"""
7. Funcție fără return, primește un string și printează pe ecran:
•	Numărul de caractere lower case este x
•	Numărul de caractere upper case exte y
"""

def numara_caractere(sir):
    lower = 0
    upper = 0

    for caracter in sir:
        if caracter.islower():
            lower += 1
        elif caracter.isupper():
            upper += 1

    print("numar caractere lower:", lower)
    print("numar caractere upper:", upper)

numara_caractere("Ala Bala Proto Cala")

"""
8. Funcție care primește o LISTĂ de numere și returnează o LISTĂ doar cu numerele pozitive.
"""
def filtreaza_numere_pozitive(lista):
    """
    :param lista: Functia preia o lista de numere negative si pozitive si filtreaza
    doar numerele pozitive
    :return: O lista cu numere pozitive
    """
    numere_pozitive = []
    for numar in lista:
        if numar > 0:
            numere_pozitive.append(numar)
    return(numere_pozitive)

numere = [1, 2, -3, -5, 9, 5, -4]
rezultat = filtreaza_numere_pozitive(numere)
print(rezultat)

"""
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZĂ
•	Primul număr x este mai mare decat al doilea număr y
•	Al doilea număr y este mai mare decat primul număr x
•	Numerele sunt egale.
"""
def compara_numere(x, y):
    if  x > y:
        print("Primul număr", x, "este mai mare decat al doilea număr", y)
    elif y > x:
        print("Al doilea număr", y, "este mai mare decat primul număr", x)
    else:
        print("Numerele sunt egale")
compara_numere(4, 6)
compara_numere(8, 6)
compara_numere(6, 6)

"""
10. Funcție care primește un număr și un set de numere.
•	Printează ‘am adaugat numărul nou în set’ + returnează True
•	Printează ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False
"""

def adauga_numar_in_set(numar, set):
    if numar in set:
        print(f"nu am adaugat {numar} în set. Acesta există deja")
        return False
    else:
        set.add(numar)
        print(f"am adaugat {numar} nou în set")
        return True

set = {1, 2, 3}
rezultat = adauga_numar_in_set(4, set)
rezultat = adauga_numar_in_set(3, set)

"""
11. Funcție care primește o lună din an și returnează câte zile are acea lună.
"""
def numar_zile_luna(luna):
    if luna == 2:
        return 28
    elif luna in [4, 6, 9, 11]:
        return 30
    else:
        return 31

numar_zile = numar_zile_luna(7)
print(numar_zile)
numar_zile = numar_zile_luna(4)
print(numar_zile)
numar_zile = numar_zile_luna(2)
print(numar_zile)

"""
12. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea, 
împărțirea a două numere.

În final vei putea face:
a, b, c, d = calculator(10, 2)
•	
"""
def calculator(a, b):
    suma = a + b
    diferenta = a - b
    inmultirea = a * b
    impartirea = a / b
    return suma, diferenta, impartirea, inmultirea

a, b, c, d = calculator(10, 3)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)

"""
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
9: 1
}
"""
def numara_aparitii_cifre(lista):
    aparitii_cifre = {} # initializam un dictionar gol
    for cifra in lista: #parcurgem ficare cifra din lista de intrare
        if cifra not in aparitii_cifre: #verifica daca cifra nu a fost intalnita pana acum in dictionar
            aparitii_cifre[cifra] = 1 # daca cifra e intalnita prima data adauga 1
        else:
            aparitii_cifre[cifra] +=1 # faca a fost gasisa de mai multe ori, adauga +1
    for cifra in range(10): # padcurge cifrele de la 0 la 9 pentru a completa dicitonarul
        if cifra not in aparitii_cifre: # daca cifra lipseste o adauga in dictionar cu valoarea zero
            aparitii_cifre[cifra] = 0
    return aparitii_cifre # afiseaza dictionarul

lista = [1, 3, 1, 5, 9, 7, 7, 5, 5]
rezultat = numara_aparitii_cifre(lista)
print(rezultat)

"""
14. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele.
"""
def gaseste_maxim(a, b, c):
    return max(a, b, c)
rezultat = gaseste_maxim(2, 4, 6)
print(rezultat)

"""
15. Funcție care să primească un număr și să returneze suma tuturor numerelor 
de la 0 la acel număr.
Exemplu: dacă dăm numărul 3, suma va fi 6 (0+1+2+3)
"""
def calculeaza_suma_pana_la(numar):
    suma = 0
    for i in range(numar + 1):
        suma += i
    return suma

rezultat = calculeaza_suma_pana_la(3)
print(rezultat)

"""
16.Funcție care primește 2 liste de numere (numerele pot fi dublate). 
Returnați numerele comune.

Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Răspuns: {2, 3}
"""

# def gaseste_numere_comune(lista1, lista2):
#     set_lista1 = set(lista1)
#     set_lista2 = set(lista2)
#     numere_comune = set_lista1.intersection(set_lista2)
#     return numere_comune
#
# lista1 = [1, 1, 2, 3]
# lista2 = [2, 2, 3, 4]
# rezultat = gaseste_numere_comune(lista1, lista2)
# print(rezultat)

"""
17. Funcție care să aplice o reducere de preț.
Dacă produsul costă 100 lei și aplicăm reducere de 10%. Pretul va fi 90 de lei.
Tratează cazurile în care reducerea e invalidă. De exemplu o reducere de 110% e invalidă.
"""
def aplica_reducere(pret, reducere):
    if reducere < 0 or reducere > 100:
        print("Reducrerea este invalida")
        return None
    else:
        pret_redus = pret * (1 - reducere/100)
        return pret_redus

pret_initial = 100
reducere = 10
pret_redus = aplica_reducere(pret_initial, reducere)
print(pret_redus)

def aplica_reducere(pret, reducere):
    if reducere < 0 or reducere > 100:
        print("Reducrerea este invalida")
        return None
    else:
        pret_redus = pret * (1 - reducere/100)
        return pret_redus

pret_initial = 100
reducere = 25
pret_redus = aplica_reducere(pret_initial, reducere)
if pret_redus is not None:
    print("Pretul redus este:", pret_redus)

"""
 18.Funcție care să afișeze data și ora curentă din România.
(bonus: afișazăi și data și ora curentă din China)
"""
import datetime
import pytz
import time

def afiseaza_data_ora():
    fus_orar_ro = pytz.timezone('Europe/Bucharest')
    data_ora_ro = datetime.datetime.now(fus_orar_ro)
    print("Data si ora in Romania este: ", data_ora_ro)

    fus_orar_cn = pytz.timezone('Asia/Shanghai')
    data_ora_cn = datetime.datetime.now(fus_orar_cn)
    print("Data si ora in China este: ", data_ora_cn)

afiseaza_data_ora()

#for i in range(10):
 #   afiseaza_data_ora()
  #  time.sleep(1)
"""
19. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la 
Crăciun dacă nu vrei să ne zici cand e ziua ta :)
"""

import datetime

def zile_pana_la_ziua_mea():
    data_curenta = datetime.date.today()
    ziua_mea = datetime.date(data_curenta.year, 8, 28)
    if ziua_mea < data_curenta:
        ziua_mea = ziua_mea.replace(year=data_curenta.year + 1)
    zile_ramase = ziua_mea - data_curenta
    return zile_ramase.days

def zile_pana_la_craciun():
    data_curenta = datetime.date.today()
    craciun = datetime.date(data_curenta.year, 12, 25)
    if craciun < data_curenta:
        craciun = craciun.replace(year=data_curenta.year + 1)
    zile_ramase = craciun - data_curenta
    return zile_ramase.days


print("Zile până la ziua mea: ", zile_pana_la_ziua_mea())
print("Zile până la Crăciun: ", zile_pana_la_craciun())



######################################
# Extra
"""
Try except
"""
def converteste_la_intreg(input_str):
    try:  # Încearcă să execute codul din interiorul blocului try
        numar = int(input_str)  # Încearcă să convertească șirul de caractere la un întreg
        return numar  # Dacă conversia reușește, returnează numărul
    except ValueError:  # Dacă conversia eșuează, se va arunca o excepție de tip ValueError
        print(f"Valoarea '{input_str}' nu poate fi convertită la un întreg.")  # Afișează un mesaj de eroare
        return None  # Returnează None pentru a indica faptul că conversia a eșuat

input_str = "123a"
numar = converteste_la_intreg(input_str)  # Apelează funcția cu un șir de caractere ce nu poate fi convertit
if numar is not None:  # Verifică dacă conversia a reușit
    print(f"Numărul convertit este {numar}.")
else:
    print("Conversia a eșuat.")




"""
args/kwargs
"""

# Definirea unei funcții care acceptă orice număr de argumente poziționale
# folosind *args. Argumentele poziționale sunt colectate într-un tuplu.
def my_function(*args):
    for arg in args:
        print(arg)  # Afisează fiecare argument pozițional

my_function(1, 2, 3, 4)

# ----------------------------------------------------------

# Definirea unei funcții care acceptă orice număr de argumente cuvinte-cheie
# folosind **kwargs. Argumentele cuvinte-cheie sunt colectate într-un dicționar.
def another_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")  # Afisează fiecare pereche cheie-valoare

another_function(a=1, b=2, c=3)

# ----------------------------------------------------------

# Combinarea *args și **kwargs pentru a accepta orice combinație de argumente
# poziționale și cuvinte-cheie.
def combined_function(*args, **kwargs):
    print("Arguments:", args)  # Afisează argumentele poziționale ca tuplu
    print("Keyword Arguments:", kwargs)  # Afisează argumentele cuvinte-cheie ca dicționar

combined_function(1, 2, a=3, b=4)






