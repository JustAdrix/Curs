'''
Metode de control in bucle :
- break: imi intrerupe bucla, iese complet din bucla - termination condition

- continue : - se continua bucla si iteratorul sare la urmatoarea valoare
                    - dar exclude conditional valorile
'''

# break
for i in range(10):
    print(i)
    if i == 5 :
        break   #opresc bucla

print('--'*30)


for nr in range(8):
    if nr == 2 :
        continue    # excludem elementul de la conditia if excludem 2-iul
    print(nr)