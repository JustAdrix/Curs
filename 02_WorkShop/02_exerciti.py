# 1.
'''
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

Folosește un for că să iterezi prin toată lista și să afișezi;
‘Mașina mea preferată este x’.
Fă același lucru cu un for each.
Fă același lucru cu un while.
'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for masina in masini:
#     print('Masina mea preferata este', {masina})

# i = 0
# while i > len(masini):
#     masini = masini[i]
#     print(masini)
#     i +=i
# 2
# for index, masina in enumerate(masini):
#     if index == 0 or index == len(masini) -1:
#         continue
#     masini[index] = masina.upper()
# else:
#     print(masini)
#
#
# # 3 Tema cu whilw
# mas = 'M'
# for client in masini:
#     if client == mas:
#         print('Am gasit masina dorita', {client})
#         break
# else:
#      print('Nu am gasit masina ', {mas}, ' mai cautam')
#
# # 5
# maini_vechi = []
# for index, maina in enumerate(masini):
#     if masina


# 6
# pret_masini = {
#     'Dacia': 6800,
#     'Lăstun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# buget = 15000
# masina = ''
# for masina, pret in pret_masini:
#     if pret <= buget:
#         print('Pentru un buget sub', {buget}, 'puteti alege',  {masina})

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0
for numar in numere:
    suma += numar
print(suma)

max = 0
for numar in numere:
    if numar > max:
        max = numar
print(max)

# 10 ... 15 Tema



