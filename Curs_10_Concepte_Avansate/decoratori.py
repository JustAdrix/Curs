'''
    Decoratorii : sunt sombinarea a trei concepte
'''


# Functii ca argumente
def say_hello(name):
    return f'Hello {name}'


def say_hi(name):
    return f'Hi {name}'


def greet_bob(func):
    return func('Bob')


print(greet_bob(say_hello))
print(greet_bob(say_hi))

print('*' * 30)


# Functii interne

def parent():
    def first():  # se pot defini functii in interiorul altor functii
        print('Hello from first')

    def secound():
        print('Hello from second')

    secound()
    first()


parent()
print('*' * 30)


# Returnare de functii

def parent(n):
    def first():
        print('First')

    def secound():
        print('Secound')

    if n == 1:
        return first
    return secound


f = parent(1)  # f -> este o functie interna
f()
print('*' * 30)

# Decoratori simpli
import functools


def my_decorator(func):
    @functools.wraps(func)  # Se adauga pentru a nu se suprascrie functia decorata cu
    # functia wrapper
    def wrapper():
        print('Ceva se inampla inainte de apelul functiei decorate')
        func()
        print('Ceva se intampla dupa apelul functiei decorata')

    return wrapper


@my_decorator
def say_we():
    print('We')


say_we()
print(say_we)
print('*' * 30)


# Decoratori pentru functii cu argumente

def do_twice(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


@do_twice
def say_salut(name):
    print(f'Salut {name}')


say_salut('Bob')
