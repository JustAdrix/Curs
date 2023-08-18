'''
    Implementați un generator pentru loteria 6/49 și noroc:
Primele 6 apelări către generator vor da cate un numar intre 1 si 49 (inclusiv
Ultima apelare va da un singur număr de “noroc” format din 7 cifre
'''
import random


def loto_generator():
    lista = random.sample(range(1, 50), 6)
    for i in lista:
        yield i
    yield random.randint(1_000_000, 9_000_000)
for val in loto_generator():
    print(val)

print('*'*40)
def loto_generator2():
    l = []
    for i in range(6):
        numar = random.randint(1, 50)
        while numar in l:
            numar = random.randint(1, 50)
        l.append(numar)
        yield numar
    yield random.randint(1_000_000, 9_000_000)
print(loto_generator2())
for numar in loto_generator2():
    print(numar)


