# a = 1/0 # ZeroDivisionError
# a = 2+b # NameError: name 'b' is not defined

#####################################################
# Aruncarea exceptiilor
x = 2
if x < 0:
    raise Exception("X este mai mic decat 0")

##################################################
# Tratarea exceptiilor
try:  # verifica un bloc de cod pentru exceptii
    print(C)
except:  # trateaza diferitele tipuri de erori
    print("A aparut o exceptie")

# --------------------------------------------------------------------------
try:
    print(1/0)
except NameError:
    print('Variabila C nu este definita')
except ZeroDivisionError as ex: # stocheaza exceptia in variabila ex
    print(f'Eroarea: {ex}')
except:
    print('Alta a fost eroarea')
#------------------------------------------------------------------------------
# ramura try, except, else este folosita pentru
try:
    print('Hello')
except:
    print("Eroare")
else:
    print("Se executa cand nu apare eroare")
# ----------------------------------------------------

try:
    print(c)
except:
    print("Eroare")
finally: # se executa de fiecare data
    print("Eu ma execut mereu")

'''
try: ( blocul try )
    bloc de cod unde ar putea aparea o eroare
    (sfrsitul blocului try )
except NumeEroare: -> prinderea tuturor exceptiilor de tipul nume eroare
                        Se executa doar daca se prinde nume erooare
except ( AltNumeEroare, IncaUnNumeEroara): -> se executa daca se prinde una din cele doua erori
except Eroare as ex: -> Stocare mesaj eroare intr-o variabila
                        Se poate accesa mesajul erorii prin variabila ex
except:
    -> Se executa pentru orice alta eroare
else:
    -> Se executa doar daca nu se arunca eroare in blocul "try"
finaly:
    -> Se: executa indiferent daca se arunca eroare sau nu

'''
