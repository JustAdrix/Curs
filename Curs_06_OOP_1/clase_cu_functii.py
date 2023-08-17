class Dog:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def bark(self): # self --> referinta catre obiectul curent ( trebuie sa apara mereu )
        print("Ham Ham")
    def get_name(self):
        return f"Eu sunt {self.name}" # accesul la atributele din clasa se face cu self. !
d=Dog (age = 5, name= "Rex")
d.bark()
print("*"*50)
print(d.get_name())