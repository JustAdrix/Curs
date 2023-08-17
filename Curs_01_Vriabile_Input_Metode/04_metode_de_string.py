# Metode de string

elf = "alpha01234567890XASD"

# Lungimea stringului :
print( len(elf))

# Replace
druid = elf.replace("alpha", "beta")
print(f"druid : {druid}")


# Proprietatea de imutabilitate  IMMUTABILITY
# se refera la faptul ca eu nu pot sa inlocuiesc valori intr-un string
elf.replace("alpha", "beta")
print(f"elf : {elf}")


# imutabilitabilitate caz 2 :
# elf[0] = "e"        # TypeError: 'str' object does not support item assignment


# nuamr de aparitii a unui string
elf.count("a")
elf.count("h")


#
nume = "kogalniceanu"
nume.upper() # transforma in litere mari
nume.capitalize() # transforma in litera mare

nume.find("ala")            # -1 inseamna non-existenta
nume.find("nic")            # arata indexul in caz ca substrigul este prezent



