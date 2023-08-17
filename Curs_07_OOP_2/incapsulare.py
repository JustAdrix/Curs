"""
Incapsularea se refera la ascunderea detaliilor de implementare ale unei clase fata
de alte clase.

Exista 3 tipuri de metode si atribute:
    -Public   ---> Accesibile peste tot
    -Protected ---> Accesibile doar in ierarhia de mostenire (_atribut) "_"
    -Private ---> Accesibile doar in clasa (__atribut) "__"

"""


class Car():
    def __init__(self, model):
        self.__model = model

    @property  # Setare ca proprietate a campulu __model
    def model(self):
        print("Setare ca proprietare...")
        return self.__model

    @model.setter
    def model(self, value):
        if value.startswith("B"):  # Restrictionare asignare valori atributului __model
            print("Nu se pot adauga modele care incep cu litera B")
            return
        print("Schimbare valoare model...")
        self.__model = value

    @model.getter
    def model(self):
        print("Returnare valoare...")
        return self.__model

    @model.deleter  # Eliberarea din memorie a valorii din campul __model
    def model(self):
        print("Stergere valoare...")
        self.__model = None


c = Car("Dacia")
print(c.model)  # se apeleaza getterul

c.model = "Volvo"  # se apeleaza setterul
print(c.model)

c.model = "BMW"
print(c.model)

del c.model  # se apeleaza deleterul
print(c.model)