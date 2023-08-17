# Lista de elemente - list [valore1, valoare2,.... ]
'''
- o insiruire de elemente ordonate
- pot avea valori diferite
- este MUTABILA ( MUTABLE ) : inseamna se pot adauga, sterge sau inlocui elemente din lista
- putem accesa orice index
- putem pune valori repetabile
- se defineste : []
'''

lista_diversa = [2, 3.14, False, 'Elefant', 12345]  # index 0:4 (4 ultimul index )
print(f'lista_diversa :  {lista_diversa}')

# Accesam elementul al 2-lea :
element2 = lista_diversa[1]
print(f'element2 : {element2}')

# Accesarea ultimului element din lista
ultimul_element = lista_diversa[-1]
print(f'ultimul_element : {ultimul_element}')

# Verificam ce lungime are lista :
lungime_lista = len(lista_diversa)
print(f'lungime_lista : {lungime_lista}')

# Incercam sa accesam un element care depaseste lungimea listei:
# un_elem = lista_diversa[5]
# print(f'un_elem : {un_elem}')


print('--' * 30)
## OPERATII cu ELEMENTE ale listei

# Inlocuirea / Schimbarea unui element din lista
lista_diversa[2] = True  # am modificat-o datorita proprietatii de mutabilitate ( este mutabila )
print(f'lista_diversa :  {lista_diversa}')

print('--' * 30)

# Adaugarea unui nou element intr-o lista
# la coada, se face cu append
lista_diversa.append('asta la vista')
print(f'lista_diversa :  {lista_diversa}')

# in interiorul listei :
lista_diversa.insert(3, 10 * 10)  # va fi al 3-lea element din lista index 2
print(f'lista_diversa :  {lista_diversa}')

# Stergerea ultimului element din lista :
lista_diversa.pop()  # .pop => sterge
print(f'lista_diversa :  {lista_diversa}')
# Stergerea unui element pe baza de index:
lista_diversa.pop(2)
print(f'lista_diversa :  {lista_diversa}')

print('--' * 30)

# LIST SLICING
# inversarea listei (::-1) :
lista_inversa = lista_diversa[::-1] # [ start stop step ]
print(f'lista_inversa :  {lista_inversa}')

# parte din lista :
# ultimele 3 elemente din lista ( -3: ):
print(f'lista_inversa ultimele 3 elemente :  {lista_inversa[-3:]}')
