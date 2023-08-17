def say_hy():
    return "Hello"


text = say_hy()
print(text)


def suma(a, b, c):
    return a + b + c


print(suma(1, 2, 3))
'''
return - 
'''


def show_bigest(a, b):
    if a > b:
        print(a)
    else:
        print(b)

b = show_bigest(1, 3)
print(b)


# daca nu specificam o valoare de return pentru o functie ea va
# returna implicit si valoarea NONE

def nimic():
    return  # daca nua are valoare returneaza NONE
print(nimic())

def end():
    return 1
    print('test') # bucata aceasta de cod nu se va rula deoarece toate
                  # functiile se opresc cand dau de cuvantul return
end()
print("*"*40)
# Exercitiu
# Sa se scrie o functie care primeste ca parametru o lista de numere
# si returneaza o lista care returneaza doar numere pare
def get_all_even_numbers(numbers):
    result = []
    for elem in numbers:
        if elem % 2 == 0:
            result.append(elem)
    return result
print(get_all_even_numbers([1,2,3,4,5,6,7,8,9,10]))
