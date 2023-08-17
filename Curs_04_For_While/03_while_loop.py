"""
    BUCLA WHILE     ( atata timp cat )
- este iterator de control
- are nevoie de o conditie de start pentru a functiona (spre deosebire de for)
- daca nu are conditie de start bucla while nu porneste
- inainte de startul buclei while, trebuie sa definim o variabila de initializare
- trebuie sa aiba si o conditie de terminare
- fara conditiile de initializare si terminare vom avea o bucla infinita

"""

nr = 0       # Initializare a variabilei
while nr <= 10 :  # conditia de rulare a buclei
    print(nr)
    nr = nr + 1       # conditia de parcurgere (incrementare )


print('--'*30)

# while True
x = 10
while True :
    print(x)
    x = x - 1
    if x == -9 :
        break


print('--'*30)

# while merge si cu else
x = 10
while x > 2 :
    print(x)
    x = x - 1
else:
    print('Sfarsitul ciclului')