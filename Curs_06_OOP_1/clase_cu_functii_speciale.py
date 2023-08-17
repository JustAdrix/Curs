class Dog:
    def __init__(self, age, name):
        self.name = name
        self.age = name
    # Magic methods / Dunder methods
    def __str__(self):
        return f"Age : {self.age}, Name : {self.name}"
    def __repr__(self):
        return str(self)  # sau return self.__str__()
    def __eq__(self, other): # comparatia se face self == other
        if not isinstance(other, Dog): # verifica daca other apartine clasei Dog
            return False
        return self.age == other.age and self.name == other.name

d=Dog(age=4, name="Rex")
d2 = Dog(age=13, name="Bruno")
print(d)
print(d2)
print("*"*30)

t = str(d)
print(t)
print("*"*30)

l=[d, d2]




print("*"*30)
d3 = Dog(1,"Puffi")
d4 = Dog(1, "Puffi")
print(d3==d4)
print(d3 == 7)

