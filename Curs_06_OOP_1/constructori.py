class Dog:
    age = 12  # atribut de clasa ( class atribute ) ==> are aceiasi valoare pentru toate obiectele din clasa
    specie = "mammal"
    name = "Rex"
    # atributele de clasa sunt in general folosite pt. a defini constante in interiorul unei clase


d = Dog()
print(d.name)  # ordinea obligatorie obiect.atribut
d2 = Dog()
d2.name = "Pufi"  # name devine atribut de instanta ( instance atribute ) pentru ca a fost modificat din obiect

print(d.name, d2.name)
Dog.name = "Bruno"
print(d.name, d2.name)


class Cat:
    species = "mammal"

    def __init__(self, age, name):  #
        self.age = age
        self.name = name


c = Cat(age=5, name="Floxi")
print(c.age, c.name)
# print(Cat.name) # incorect deoarece un atribut de instanta poate fi accesat doar printrun obiect
