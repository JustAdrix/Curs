"""
Program care verifica input-ul de la tastatura

"""

"""
DEFINIREA EXACTA A PROBLEMEI :
1. Vrem ca sa verificam ca inputul de la keyboard ( tastatura ) sa fie de tip FLOAT, 
moment in care sa se opreasca
2. Daca nu este de tip FLOAT, continua bucla while (la nesfarsit)
3. Sa se inmulteasca rezultatul cu 5
4 . Sa imi printeze INT fara zecimale, iar float cu zecimale

"""

while True:
    numar = input("prompter: ")
    # fie numar este INT - prima conditie inainte de or
    # fie numar este FLOAT - conditia compusa dupa or
    if numar.isnumeric() is True or (numar.count('.') == 1 and numar.replace('.', '0').isnumeric() is True):
        print(f"Da, acesta este un numar : {numar}")
        inmultire = float(numar) * 5
        if inmultire % 1 == 0:
            print(f'Inmultit cu 5, int = {int(inmultire)}')
        else:
            print(f'Inmultit cu 5, float = {inmultire}')

        break
    else:
        print(f"imi pare rau, {numar} nu este un numar")
        print('mai incearca odata')


