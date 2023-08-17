def plus(a, b):  # a si b sunt parametri ( numele folosite pentru argumentele unei functii
    return a + b


plus(1, 2)  # 1 si 2 sunt argumente ( argumentele sunt valorile parametrilor)


##################################################################

# default arguments ( parametri cu valori implicite )
def plus(a, b=1):
    return a + b


plus(1)  # daca nu specificam o valoare pentru b va lua valoarea implicita 1
plus(1, 3)


################################################################
# Keword arguments ( argumente cu nume )
def plus_keyword(a, b):
    return a + b


plus_keyword(a=1, b=2)
plus_keyword(b=2, a=1)  # specificand argumentele prin nume


# nu mai este necesat sa respectam ordinea lor
##########################################################################

# Variabal number of arguments ( numar variabil de argumente )

def plus_many(*args):
    print(args)
    return sum(args)


plus_many(1, 2, 3)
plus_many()
plus_many(*[1, 2, 3])  # * - se numeste unpacking


def plus_many_2(**kwargs):
    print(kwargs)
    return sum(kwargs.values())


print(plus_many_2(a=1, b=2))
print(plus_many_2(k=5, x=17))


def plus_many3(*args, **kwargs):
    print(args, kwargs)
    return sum(args) + sum(kwargs.values())


plus_many3(1, 2, 3, a=4, b=5, c=6)
plus_many3(1, 2)
plus_many3(a=7, b=8)
plus_many3()
# plus_many3(a=1,3) -> parametri pozitionali pot fi pusi doar inainte de cei cu nume
