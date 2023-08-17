'''

ITERATORI ( BUCLE REPETITIVE )

- este un obiect care poate fi iterat ( parcurs un element cate un element, unu cate unu )
Ex : lista, tuple, set, dict, string
    ( nu pot fi iterate : Bool, Int, Float )
- contin un numar de valori care se pot numara (itera)

'''

fructe = ['mar', 'para', 'banana', 'portocala', 'cireasa']
print(f"fructe : {fructe}")

print('--'*30)

for fruct in fructe:
    print(fruct, end=', ')      # printam pe o singura linie
    # print(fruct)

print('\n','--'*30)     # \n - new line ( linie noua )


for fructul_meu in fructe:      # for poate avea else la sfarsit ca si alternativa de terminare
    print(f"fructul_meu = {fructul_meu}")
else :
    print("Am terminat bucla repetitiva for.")          #  ( este o Particularitate Python )


print('--'*30)

# FOR in conjunctie cu if

lista_mixta= ["avocado", 2023, True, 5.66, "Mihai", (11, 12) ]

for elem in lista_mixta:
    if type(elem) is str:
        elem = elem.upper()
        print(elem)
    else:
        print(f"{elem} nu este un string")


print('--'*30)

# Iteratie la numere :

for numar in range(1, 11):      # in functia range ultimul numar nu este accesat
    print(numar)

print('--'*30)

for numar in range(10, 0, -1):      # parcurgem descrescator
    print(numar, end=', ')
print()

print('--'*30)

# cea mai simpla iteratie posibila :
for i in range(5):
    print(i)