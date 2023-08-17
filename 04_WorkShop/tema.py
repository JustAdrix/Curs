'''
19. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
 Crăciun dacă nu vrei să ne zici cand e ziua ta :)
'''
import datetime

# import datetime
# def zile_pama_la_ziua_mea():
#     data_curenta = datetime.date.today()
#     ziua_mea = datetime.date(data_curenta.year, 10, 23)
#     zile_ramase = ziua_mea - data_curenta
#     return zile_ramase
# def zile_pana_la_craciun():
#     data_curenta_1 = datetime.date.today()
#     craciun = datetime.date(data_curenta_1.year, 12, 25)
#     zile_ramase = craciun - data_curenta_1
#     return zile_ramase
# print(zile_pama_la_ziua_mea())
# print(zile_pana_la_craciun())
#
# def converteste_la_intreg(input_str):
#     try:  # Încearcă să execute codul din interiorul blocului try
#         numar = int(input_str)  # Încearcă să convertească șirul de caractere la un întreg
#         return numar  # Dacă conversia reușește, returnează numărul
#     except ValueError:  # Dacă conversia eșuează, se va arunca o excepție de tip ValueError
#         print(f"Valoarea '{input_str}' nu poate fi convertită la un întreg.")  # Afișează un mesaj de eroare
#         return None  # Returnează None pentru a indica faptul că conversia a eșuat
#
# input_str = input("Introducetii un string : ")
# numar = converteste_la_intreg(input_str)  # Apelează funcția cu un șir de caractere ce nu poate fi convertit
# if numar is not None:  # Verifică dacă conversia a reușit
#     print(f"Numărul convertit este {numar}.")
# else:
#     print("Conversia a eșuat.")

'''
1.Clasa Cerc
    Atribute: rază, culoare
    Constructor pentru ambele atribute
    Metode:
descrie_cerc() - va PRINTA culoarea și raza
aria() - va RETURNA aria 
diametru() 
circumferinta()

'''
# import math
#
#
# class Cerc():
#     def __init__(self, raza, culoare):
#         self.raza = raza
#         self.culoare = culoare
#
#     def descriere_cerc(self):
#         return f'Cercul este {self.culoare}, si are reza de {self.raza}'
#
#     def aria(self):
#         return math.pi * self.raza ** 2
#
#     def diametrul(self):
#         return self.raza * 2
#
#     def circumferinta(self):
#         return math.pi * 2 * self.raza
#
#
# cerc1 = Cerc(5, 'Rosu')
# cerc2 = Cerc(10, 'Mov')
# print(cerc1.descriere_cerc())
# print(f'Aria este : {cerc1.aria()}')
# print(f"Diametrul este : {cerc1.diametrul()}")
# print(f"Circumferinta este : {cerc1.circumferinta()}")
# print(cerc2.descriere_cerc())
# print(f'Aria este : {cerc2.aria()}')
# print(f"Diametrul este : {cerc2.diametrul()}")
# print(f"Circumferinta este : {cerc2.circumferinta()}")
'''
2. Clasa Dreptunghi
     Atribute: lungime, lățime, culoare
     Constructor pentru toate atributele
     Metode:
descrie()
aria()
perimetrul()
schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare.
Poți verifica schimbarea culorii prin apelarea metodei descrie().

'''
# class Dreptunghi:
#     def __init__(self, lungime, latime, culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#     def descriere(self):
#         return f'Dreptunghiul are lungimea de {self.lungime}, latimea de {self.latime}, si culoarea {self.culoare}'
#     def aria(self):
#         return  self.latime*self.lungime
#     def perimetru(self):
#         return (self.lungime+self.latime)*2
#     def schimba_culoarea(self, culoare_noua):
#         self.culoare = culoare_noua
#         print(f'Noua culoare este : {culoare_noua}')
#
# d1 = Dreptunghi(10,15,'Albastru')
# print(d1.descriere())
# print(f'Aria este = {d1.aria()}')
# print(f'Perimetrul este = {d1.perimetru()}')
# d1.schimba_culoarea('Verde')
# print(d1.descriere())

'''
3. Clasa Angajat
     Atribute: nume, prenume, salariu
     Constructor pentru toate atributele
     Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)

'''
# class Angajat:
#     def __init__(self,nume, prenume,salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#     def descriere(self):
#         return f'\n Nume : {self.nume} \n Prenume : {self.prenume} \n Salariu {self.salariu}'
#     def nume_complect(self):
#         return f'Nume complet : {self.prenume} {self.nume}'
#     def salariu_lunar(self):
#         return  f'Salariul este : {self.salariu} lei / luna'
#     def salariu_anual(self):
#         return f'Salariul anual este : {self.salariu*12} lei'
#     def marire_salariu(self, procent):
#         self.procent = procent
#         return f'Slariul lunar marit cu {self.procent}% este : {self.salariu+(self.salariu*(self.procent/100))} lei'
# angajat = Angajat('Ionescu','Andrei', 5000)
# print(angajat.descriere())
# print(angajat.nume_complect())
# print(angajat.salariu_lunar())
# print(angajat.salariu_anual())
# print(angajat.marire_salariu(20))

'''
4. Clasa Cont
   Atribute: iban, titular_cont, sold
   Constructor pentru toate atributele
   Metode:
afisare_sold() - Titularul x are în contul y suma de n lei
debitare_cont(suma)
creditare_cont(suma)

'''
# class Cont:
#     def __init__(self,iban, titular_cont, sold):
#         self.iban = iban
#         self.titular_cont = titular_cont
#         self.sold = sold
#     def afisare_sold(self):
#         return f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei'
#     def debitare_cont(self,suma):
#         if suma > self.sold:
#             print('Fonduri insuficiente')
#         else:
#             self.sold -= suma
#             return suma
#     def creditare_cont(self,suma):
#         self.sold += suma
#         return suma
# cont = Cont ('RO7854RNCB09756432', 'Adrian Holom', 100000)
# print(cont.afisare_sold())
# print(f'S-au debitat {cont.debitare_cont(2)}')
# print(cont.afisare_sold())
# print(f'S-au creditat {cont.creditare_cont(500)}')
# print(cont.afisare_sold())

'''
5. Clasa Factură
     Atribute: seria (va fi constantă, nu trebuie constructor,
    toate facturile vor avea aceeași serie), număr, nume_produs, cantitate, pret_buc
     Constructor: toate atributele, fără serie
     Metode:
schimbă_cantitatea(cantitate)
schimbă_prețul(pret)
schimbă_nume_produs(nume)
generează_factura() - va printa tabelar dacă reușiți

Factura seria x număr y
Data: generează automat data de azi
Produs | cantitate | preț bucată | Total 
Telefon |      7       |       700       | 49000     

'''
from tabulate import tabulate
class Factura:
    serie = 'FAC'

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate_noua):
        self.cantitate = cantitate_noua

    def schimba_pret(self, pret_nou):
        self.pret_buc = pret_nou

    def schimba_nume_pordus(self, nume_produs_nou):
        self.nume_produs = nume_produs_nou

    def genereaza_factura(self):
        data = datetime.date.today().strftime("%d.%m.%Y") # formatare data ( % - orice )
        total = self.cantitate * self.pret_buc

        # print(f'Factura seria: {Factura.serie} numar: {self.numar} \n Data {data} ')
        # print("Produs | Cantitate | Preț bucată | Total")
        # print(f'{self.nume_produs} | {self.cantitate} | {self.pret_buc} | {self.cantitate * self.pret_buc}')
        # print("Factura seria", Factura.serie, "numarul", self.numar)
        # print("Data:", data)
        # print("Produs\t|\tCantitate\t|\tPret bucata\t|\tTotal")
        # print(self.nume_produs, "\t|\t", self.cantitate, "\t\t|\t", self.pret_buc, "\t\t|\t", total)
        header = ["Produs", "Cantitate","Pret bucata", "Total"]
        col_names = [[self.nume_produs, self.cantitate, self.pret_buc, total]]
        print("Factura seria", Factura.serie, "numarul", self.numar)
        print("Data:", data)
        print(tabulate(col_names, headers=header, tablefmt="grid"))
fact1 = Factura(1, 'Telefon', 3, 1000)
fact2 = Factura(2, 'Televizor', 4, 2500)
print(fact1.genereaza_factura())
print(fact2.genereaza_factura())
print('*'*40)
fact1.schimba_pret(1500)
print(fact1.genereaza_factura())
print('*'*40)
fact2.schimba_cantitatea(10)
print(fact2.genereaza_factura())
print('*'*40)
fact1.schimba_nume_pordus('Avion')
print(fact1.genereaza_factura())

