'''
13. Exercițiu:
citește un string de la tastatură (ex: alabala portocala);
salvează primul caracter într-o variabilă - indiferent care
este el, încearcă cu 2 stringuri diferite;
 capitalizează acest caracter peste tot, mai puțin pentru primul
și ultimul caracter => alAbAlA portocAla.
'''

text = "blabala portocblb"
primul_caracter = text[0]
rezultat = ''
print(text)
for caracter in text:
    if caracter == primul_caracter:
        rezultat += caracter.upper()
    else:
        rezultat += caracter
print(rezultat[0].lower()+rezultat[1:-1]+rezultat[-1].lower())



