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

jucatori_teren = ['j1', 'j2', 'j3', 'j4', 'j5']
schimbari_efectuate = 0
schimbari_max = 3
print('In teren', jucatori_teren)
jucator_out = input('Schimbati jucatorul ')
jucator_in = input('Intra jucatorul')
if jucator_out in jucatori_teren and schimbari_max != 0:
    index = jucatori_teren.index(jucator_out)
    jucatori_teren.pop(index)
    jucatori_teren.insert(index, jucator_in)
    schimbari_max -= 1
    print('A intrat  : ', jucator_in, 'a iesit : ', jucator_out, 'si mai ai :  ', schimbari_max, 'schimbari')
else:
   print('nu se poate efectua schimbarea deoarece jucătorul : ',jucator_in, ' nu este in teren' )
   print('Mai aveti : ', schimbari_max, ' schimbari')
#
#
# x = int(input("Introduceti un numar intreg:"))
#
# if x >= 1000 and x < 9999:
#     print("True")
# else:
#     print("False")
