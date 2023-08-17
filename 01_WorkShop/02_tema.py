'''
9. Citește o literă de la tastatură.
    Verifică și afișează dacă este vocală sau nu.

'''
# import random

'''
litera = input("Introduceti o litera : ")
vocale = ['a', 'e', 'i', 'o', 'u']
if len(litera) == 1:
    if litera.lower() in vocale:
        print('Litera ', litera + ' este o vocala')
    else:
        print('Litera ', litera + ' este o consoana')
else:
    print('Ati intordus mai multe litere !!! ')
'''
print('*'* 40)

'''
10. Transformă și printează notele din sistem românesc în  >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
'''
'''
nota = float(input('Introduceti nota'))
if nota < 10:
    if nota >= 9:
        print(f'Echivalentul notei : ', {nota}, ' este A')
    elif nota >= 8:
        print(f'Echivalentul notei : ', {nota}, ' este B')
    elif nota >= 7:
        print(f'Echivalentul notei : ', {nota}, ' este C')
    elif nota >= 6:
        print(f'Echivalentul notei : ', {nota}, ' este D')
    elif nota >= 5:
        print(f'Echivalentul notei : ', {nota}, ' este E')
    else:
        print(f'Echivalentul notei : ', {nota}, 'este F')
else:
    print('Nota nu este valida')
'''

print('*'* 40)

'''
11.Verifică dacă x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)

'''
'''
x = int(input('Introduceti un numar din minim 4 cifre : '))
if x < 999:
    print(x,' are mai putin de 4 cifre !!!')
else:
    print(x, 'are peste 4 cifre')
'''

print('*'* 40)
'''
12.Verifică dacă x are exact 6 cifre.
'''

'''
x = int(input('Introduceti un numar din 6 cifre : '))
x_string = str(x)
if len(x_string) != 6:
    print(x,' Nu are 6 cifre !!!')
else:
    print(x, 'are 6 cifre')
'''

print('*'* 40)

'''
13.Verifică dacă x este număr par sau impar (x e int).

'''
'''
x = int(input('Introduceti un numar : '))
if x %2 == 0:
    print(x, 'este par')
else:
    print(x, ' este impar')
'''
print('*'* 40)
'''
14.      x, y, z (int)
Afișează care este cel mai mare dintre ele?

'''

'''
x = int(input('Introduceti x : '))
y = int(input('Introduceti y : '))
z = int(input('Introduceti z : '))
cel_mai_mare = max(x,y,z)
print(cel_mai_mare, ' este cel mai mare numar')
'''
print('*'* 40)

'''
15. 
X, y, z - reprezintă unghiurile unui triunghi
Verifică și afișează dacă triunghiul este valid sau nu.
'''
'''
x = float(input('Introduceti marimea unghiului x : '))
y = float(input('Introduceti marimea unghiului y : '))
z = float(input('Introduceti marimea unghiului z : '))
if x+y+z == 180:
    print('Triunghiul este valid')
else:
    print('Triunghiul nu este valid')
'''
print('*'* 40)

'''
16. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
Citește de la tastatură un int x
Afișează stringul fără ultimele x caractere
Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'
'''
'''
text = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('Introduceti un numar'))
lungime_text = len(text)
print(text)
if x <= lungime_text:
    print(text[0:-1-x])
else:
    print('Numarul introdus este prea mare')
'''
print('*'*40)

'''
17. Același string. Declară un string nou care să fie format din primele 5 
caractere + ultimele 5.

'''
'''
text = 'Coral is either the stupidest animal or the smartest rock'
lungime_text = len(text)
print(text)
print(text[0:5:] + text[lungime_text-5:lungime_text])
'''

print('*'*40)

'''
18. Același string. 
Salvează într-o variabilă și afișează indexul de start al cuvântului rock 
(hint: este o funcție care te ajuta sa faci asta)
Folosind această variabilă + slicing, afișează tot stringul până la acest cuvânt
output: 'Coral is either the stupidest animal or the smartest' 

'''
'''
text = 'Coral is either the stupidest animal or the smartest rock'
index_rock = text.index('rock')
print(text[0:index_rock])
'''
print('*'*40)
'''
19. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Ia numărul ghicit de la utilizator
Verifică și afișează dacă utilizatorul a ghicit
Vei avea 3 opțiuni
Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
Ai ghicit. Felicitări! Ai ales x si zarul a fost y.

'''
# import random
# dice_roll = random.randint(1, 6)
# numar_ales = int(input('Alegeti un numar intre 1 si 6 : '))
#
# if numar_ales <= 6:
#     print('Zarul are valoarea:', dice_roll)
#     if dice_roll > numar_ales:
#         print('Ai pierdut. Ai ales un numar mai mic. Ai ales', numar_ales, 'dar a fost', dice_roll)
#     elif dice_roll < numar_ales:
#         print('Ai pierdut. Ai ales un numar mai mare. Ai ales', numar_ales, 'dar a fost', dice_roll)
#     else:
#         print('Ai ghicit. Felicitări! Ai ales', numar_ales, 'si zarul a fost', dice_roll)
# else:
#     print('Numarul ales este prea mare!')
#
print('*'*40)
'''
20.  Citește de la tastatură un string
Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat

'''

# text = input('Introduceti un text : ')
# print(text)
# assert text.lower()[0] == text.lower()[-1], 'Primul si ultimul caracter sunt diferite'

print('*'*40)
'''
21. Având stringul '0123456789'
Afișează doar numerele pare 
Afișează doar numerele impare
(hint: folosește slicing, controlează din pas)

'''
'''
numere = '0123456789'
lungime_text = len(numere) # doarece slicing [inceput(inclusiv):sfarsit(exclusiv):pas)
numere_pare = numere[2:lungime_text:2]
numere_impare = numere[1:lungime_text:2]
print(numere)
print(numere_pare)
print(numere_impare)
'''
