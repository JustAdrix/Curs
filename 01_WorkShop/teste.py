import datetime

def verifica_varsta():
    an_nastere = int(input("Introduceți anul nașterii: "))
    an_actual = datetime.date.today().year
    varsta = an_actual - an_nastere

    if varsta >= 18:
        print("Acces permis...")
    else:
        print("Acces restricționat. Trebuie să aveți cel puțin 18 ani.")

verifica_varsta()