"""
Clasă Student:
Creați o clasă numită "Student" pentru a reprezenta un student.
Clasa ar trebui să aibă atribute precum nume, prenume, varsta, nota_mate și nota_info.
Adăugați metode pentru a calcula media notelor și pentru a verifica dacă studentul a trecut examenul
 (media notelor este mai mare sau egală cu 5).
"""


class Student():
    def __init__(self, nume, prenume, varsta, nota_mate, nota_info):
        self.nume = nume
        self.prenume = prenume
        self.varsta = varsta
        self.nota_mate = nota_mate
        self.nota_info = nota_info

    def media_notelor(self):
        self.media = (self.nota_mate + self.nota_info) / 2
        print(f"Media studentului {self.prenume} {self.nume} este {self.media}")
        return self.media

    def admis_respins(self):
        if self.media >= 5:
            print(f"Studentul {self.prenume} {self.nume} este admis cu media: {self.media}")
            return True
        elif self.media == 4.5:
            print(f"Studentul {self.prenume} {self.nume} este admis cu media: {self.media} prin rotunjire catre 5")
            return True
        else:
            print(f"Studentul {self.prenume} {self.nume} este respins cu media: {self.media}")
            return False


student1 = Student("Ionescu", "Vlad", 22, 5, 4)
student1.media_notelor()
student1.admis_respins()
print("*" * 60)

student2 = Student("Popescu", "Ionut", 20, 5, 10)
student2.media_notelor()
student2.admis_respins()
print("*" * 60)

student3 = Student("Amadeus", "Florin", 23, 3, 4)
student3.media_notelor()
student3.admis_respins()
print("*" * 60)

"""
Clasă Calculator:
Implementați o clasă "Calculator" care să aibă metode pentru operații de bază precum
adunare, scădere, înmulțire și împărțire.
Asigurați-vă că clasa poate gestiona și numere zecimale.
"""


class Calculator():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def adunare(self):
        rezultat_adunare = self.a + self.b
        print(f"Rezultatul adunarii lui {self.a} si {self.b} este: {float(rezultat_adunare)}")
        return float(rezultat_adunare)

    def scadere(self):
        rezultat_scadere = self.a - self.b
        print(f"Rezultatul scaderii lui {self.a} cu {self.b} este: {float(rezultat_scadere)}")
        return float(rezultat_scadere)

    def inmultire(self):
        rezultat_inmultire = self.a * self.b
        print(f"Rezultatul inmultirii lui {self.a} cu {self.b} este: {float(rezultat_inmultire)}")
        return float(rezultat_inmultire)

    def impartire(self):
        rezultat_impartire = self.a / self.b
        print(f"Rezultatul impartirii lui {self.a} cu {self.b} este: {float(rezultat_impartire)}")


operatori1 = Calculator(7, 3.5)
operatori1.adunare()
operatori1.scadere()
operatori1.inmultire()
operatori1.impartire()

print("*" * 60)

"""
Clasă Călătorie:
Creați o clasă "Călătorie" pentru a urmări informații despre călătorii. 
Clasa ar trebui să aibă atribute precum destinatie, data, durata și cost. 
Adăugați metode pentru a calcula data de întoarcere și pentru a afișa detalii despre călătorie.
"""

from datetime import datetime, timedelta

class Calatorie():
    def __init__(self, destinatie, data, durata, cost):
        self.destinate = destinatie
        self.data = data
        self.durata = durata
        self.cost = cost

    def data_intoarcere(self):
        data_intoarcerii = self.data + self.durata
        print(f"Intoarcerea din calatorie se va face in {data_intoarcerii}")
        return data_intoarcerii
    def date_despre_calatorie(self):
        print(f"Aceasta calatorie este catre {self.destinate}, se pleaca in {self.data}, dureaza {self.durata} si costa {self.cost}")


calatorie1 = Calatorie("Italia",datetime(2023,8,15), timedelta(weeks=3.2), "1500 Euro")
calatorie1.date_despre_calatorie()
calatorie1.data_intoarcere()