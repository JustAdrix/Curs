class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def print_name(self):
        print(f'My name is {self.name}')


class Student(Person):
    pass


p = Person(30, 'Toni')
p.print_name()
s = Student(22, 'Andy')
s.print_name()

print("*" * 30)


class Angajat(Person):
    def __init__(self, age, name, loc_de_munca):
        super().__init__(age, name) # este direct o referinta catre clasa parinte
        self.loc_de_munca = loc_de_munca

    def print_work(self):
        print(f'Lucrez la {self.loc_de_munca}')
a= Angajat(30, 'Jhon', 'Amazon')
a.print_name()
a.print_work()

print("*" * 30)