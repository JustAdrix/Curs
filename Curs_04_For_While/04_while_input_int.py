
"""
Program care verifica input-ul de la tastatura

"""

"""
DEFINIREA EXACTA A PROBLEMEI :
1. Vrem ca sa verificam ca inputul de la keyboard ( tastatura ) sa fie de tip INT, 
moment in care sa se opreasca
2. Daca nu este de tip INT, continua bucla while (la nesfarsit)

"""

while True:
    numar = input("prompter: ")
    if numar.isnumeric() : # isnumeric functioneaza doar pentru INT
        print(f"Da, acesta este un numar : {numar}")
        print(f'Inmultit cu 5 = {float(numar) * 5}')
        break
    else:
        print(f"imi pare rau, {numar} nu este un numar")
        print('mai incearca odata')


