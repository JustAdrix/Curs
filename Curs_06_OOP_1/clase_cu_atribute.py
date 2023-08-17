class Dog:
    age = 12
    specie = "mammal"
    name = "Rex"
print(Dog.age) # --> accesare atribute direct prin clasa lor
print(Dog.specie)

d = Dog() # --> crearea unui obiect ( instanta ) din clasa Dog
print(d.age, d.name, d.specie)

'''
In exemplul de mai sus, vaariabila d este o instanta a clasei Dog
iar Dog 
'''
class Dog:
    age = 12
    species = "mammal"
    name = "Rex"


print(Dog.age)  # --> accesare atribute direct prin referire la clasa lor
print(Dog.species)
print("*" * 50)
d = Dog()  # --> crearea unui obiect (instanta) din clasa Dog
print(d.age, d.name, d.species)

"""
In exemplul de mai sus, variabila d este o instanta a clasei Dog,
iar Dog este o clasa, deci defineste un nou tip de data


Prin obiectul d, se pot accesa toate atributele clasei Dog
"""