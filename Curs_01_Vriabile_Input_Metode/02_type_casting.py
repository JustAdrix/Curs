
# functia type - returneaza tipul variabilei sau al datei

nume_complet, prenume = "Ion Creanga", True

print(type(nume_complet))
print(type(prenume))


# TYPE CASTING - Schimbarea tipului de variabila

x = 2.7172
print(type(x))

x = str(x)          # pt ca int(), str(), float()
print(type(x))

y = "Eminescu"
y = int(y)  # Eroare pentru ca nu poate sa transforme literele in cifre ; ValueError: invalid literal for int() with base 10: 'Eminescu'