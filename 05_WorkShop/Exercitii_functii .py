"""
Salut, Funcție!
Defină o funcție numită salut care primește un parametru nume
 și afișează un mesaj de salut specific pentru acel nume.
 Apoi, apelează funcția pentru a saluta diferite persoane.
"""

def salut(nume):
    print(f"Salut, {nume}")

salut("Mihai")
salut("Vlad")

print("*"* 60)
"""
Calculul Lungimii Șirului
Defină o funcție numită lungime_sir care primește un șir de caractere și returnează lungimea acestuia. 
Apoi, citește un șir de la tastatură și afișează lungimea sa folosind funcția.
"""

def lungime_sir(text):
    print(len(text))

lungime_sir("Habar")
lungime_sir("Habar nu am")

print("*"* 60)
"""
Verificarea Numărului Par/Impar
Defină o funcție numită este_par care primește un număr întreg 
și returnează True dacă numărul este par și False dacă este impar. 
Apoi, citește un număr de la tastatură și afișează dacă este par sau impar folosind funcția.
"""

def este_par(numar):
    if numar % 2 == 0 :
        print(f"Numarul {numar} este par")
        return True
    else:
        print(f"Numarul {numar} NU este par")
        return False
rezultat = este_par(6142214)
print(rezultat)

print("*"* 60)
"""
Concatenarea Șirurilor
Defineste o funcție numită concateneaza care primește două șiruri 
de caractere și returnează un șir rezultat din concatenarea lor.
 Apoi, apelează funcția cu două șiruri și afișează rezultatul.
"""

def concatoneaza(sir1, sir2):
    rezultat = sir1 + sir2
    return rezultat

print(concatoneaza("EuSuntSir1", "EuSuntSir2"))

print("*"* 60)
"""
Calculul Mediei
Defineste o funcție numită media care primește o listă de numere și returnează media lor. 
"""

def media(x):
    rezultat = sum(x) / len(x)
    return rezultat
print(media([2,4,6,8,10]))

print("*"* 60)
"""
Verificarea Palindromului
Defină o funcție numită este_palindrom care primește un șir de caractere și 
returnează True dacă șirul este palindrom (se citește la fel de la stânga la dreapta și de la dreapta la stânga) 
sau False în caz contrar.
Apoi, citește un șir de la tastatură și afișează rezultatul verificării.
"""

def este_palindrom(y: str):
    cuvant_inversat = y[::-1]
    if y == cuvant_inversat:
        print(f"Da, cuvantul {y} este palindrom ")
        return True
    else:
        print(f"Nu, cuvantul {y} nu este palindrom")
        return False

# raspuns = input("Adauga un cuvant care crezi ca este palindrom: ")   #linie anulata prin comentariu
# este_palindrom(raspuns)  #linie anulata prin comentariu
print(este_palindrom("civic"))

print("*"* 60)
"""
Calculul Puterii
Defineste o funcție numită putere care primește doi parametri, baza și exponent, 
și returnează rezultatul ridicării la putere. 
Apoi, citește doua numere de la tastatură și afișează rezultatul folosind funcția.
"""
def putere(baza, exponent):
    rezultat = baza ** exponent
    print(rezultat)
    return rezultat

while True:
    raspuns_baza = input("Alege un numar ca si baza: ")
    if not raspuns_baza.isdigit():
        print("Caracterul introdus nu este un numar. Te rog sa introduci un numar.")
    else:
        break  # Ieși din buclă dacă caracterul introdus este un număr

raspuns_baza = int(raspuns_baza)  # Converteste caracterul introdus la int

while True:
    raspuns_exponent = input("Alege un numar ca si exponent: ")
    if not raspuns_exponent.isdigit():
        print("Caracterul introdus nu este un numar. Te rog sa introduci un numar.")
    else:
        break #Iesi din bucla daca caracterul introdus este un numar

raspuns_exponent = int(raspuns_exponent) #convertire la INT

putere(raspuns_baza, raspuns_exponent)

