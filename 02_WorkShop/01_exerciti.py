# 1
# note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# print(note_muzicale)
#
# # inversate
# note_muzicale = note_muzicale[::-1]
# print(note_muzicale)
# note_muzicale.reverse()
# print('Lista initala : ', note_muzicale)

# 2
# note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# nr_apariti = note_muzicale.count('do')
# print(nr_apariti)

# 3
lista_1 = [2, 1, 0, 2]
lista_2 = [6, 5, 4]
varianta_1 = lista_1 + lista_2
print(varianta_1)

varianta_2 = lista_1.copy()
varianta_2.extend(lista_2)
lista_1.extend(lista_2)

print(varianta_2)
print(lista_1)

# 4
# sortare
sortare_lista = lista_1.sort()
print(lista_1)

# 5
# stargem 0
varianta_1.remove(0)
print(varianta_1)

# 6
# Verifica lista de la 3 cu if
lista_1 = [2, 1, 0, 2]
if len(lista_1) == 0:

    print('Lista este goala')
else:
    print(f'Lista are ', len(lista_1))
lista_1.clear()

#7

# 8
#dictionar = {'Ana' : [8, 9, 10], 'Gigel' : 10, 'Dorel' : 5}
# for elev in dictionar.keys(10)

# 9
#for elev, nota in dictionar.items():
#   print(elev, 'a luat nota', nota) #####
 # 10

#
# del dictionar['Gigel']
#
# dictionar['Ionica'] = 9
#
#
# print(dictionar)
#
# # 12
#
# dictionar.pop()

'''
12. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:

Declară o Listă cu 5 jucători
Schimbari_efectuate = te joci tu cu valori diferite
Schimbari_max = 3

Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
Efectuează schimbarea 
Șterge jucătorul scos din listă
Adaugă jucătorul intrat
Afișază a intrat x, a ieșit y, mai ai z schimbări

Dacă jucătorul nu e în teren:
Afișază ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în teren’
Afișază ‘mai ai z schimbări’

Testează codul cu diferite valori

Google search hint
“how to check if item is în list python”



'''
12 # tema
jucatori_teren = ['j1', 'j2', 'j3', 'j4', 'j5']
schimbari_efectuate = 0
schimbari_max = 3
#jucator_rez = ['j7', 'j8', 'j9']
print('In teren', jucatori_teren)
jucator_out = input('Schimbati jucatorul ')
jucator_in = input('Intra jucatorul')
if jucator_out in jucatori_teren and schimbari_max != 0:
    n = jucatori_teren.remove(jucator_out)
    print(n)
    print(jucatori_teren)
    schimbari_efectuate -= schimbari_max
    print('Jucatori din teren sunt : ', {jucatori_teren}, 'si mai aveti',{schimbari_efectuate},
          ' schimbari')
else:
    print('Nu se poate schimba jucatorul introdus')


# 14

