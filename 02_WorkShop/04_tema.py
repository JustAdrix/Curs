# 9
'''
Iterează prin ea.
Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
Afișază noua listă.
'''

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# numere_new = []
# for numar in numere:
#     if numar > 0:
#         numere_new.append(-numar)
#     else:
#         numere_new.append(numar)
# print(numere)
# print(numere_new)

# 11
'''
Itereaza prin listă alte_numere 
Populează corect celelalte liste
Afișează cele 4 liste la final
'''

# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# for n in alte_numere:
#     if n % 2 == 0:
#          numere_pare.append(n)
#     if n % 2 != 0:
#         numere_impare.append(n)
#     if n > 0:
#         numere_pozitive.append(n)
#     if n < 0:
#         numere_negative.append(n)
# print(alte_numere)
# print('Numere pare : ', numere_pare)
# print('Numere impare : ', numere_impare)
# print('Numere pozitive : ', numere_pozitive)
# print('Numere negative', numere_negative)

print('*'*30)
# 12
'''
12. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
'''
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# print(alte_numere)
# for index_1 in range(len(alte_numere)):
#     for index_2 in range(index_1+1):
#         if alte_numere[index_1] < alte_numere[index_2]:
#              alte_numere[index_1], alte_numere[index_2] = alte_numere[index_2], alte_numere[index_1]
# print('Noua lista este : ', alte_numere)

print('*'*30)

# 13
'''
. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
   User alege un număr
   Programul îi spune:
Nr secret e mai mare
Nr secret e mai mic
Felicitări! Ai ghicit!
'''
# import random
# numar_secret = random.randint(1, 30)
# # print(numar_secret)
# while numar_secret == numar_secret :
#     numar_ghicit = int(input('Introduceti un numar : '))
#     if numar_ghicit < numar_secret:
#         print('Nr secret este mai mare ')
#     elif numar_ghicit > numar_secret:
#         print('Nr secret este mai mic ')
#     else:
#         print('Felicitari! Ai ghicit')
#         break
# # 14
'''
4. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777
'''

# a = int(input('Introduceti un numar : '))
# for b in range(1, a + 1):
#     for c in range(b):
#         print(b, end="")
#     print('')
# 15
'''
terează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)
'''

tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
for t in tastatura_telefon:
    print(t)
    for x in t:
        print('Cifra curenta este : ', x)

lista_2d = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]

print(lista_2d[0]) # index de la lista mama
print(lista_2d[2][1]) # primul index de la lista mama [1], al 2-lea index [1] din sublista