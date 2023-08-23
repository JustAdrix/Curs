'''
Serializarea Datelor ->> se doreste persistarea ( salvarea ) datelor din aplicatie pentru a fi
                        disponibile ii viitor pentru a putea fi citite sau modificate
'''

# Citire date in mod clasic

def read_clasic():
    f = open("data.txt", "r") # deschiderea fisierului si retinerea in variabila "f"
    try:
        return f.readlines() # citim toate datele din fiser
    except Exception as ex:
        print(f'Error : {ex}')
    finally:
        f.close() # inchidem fisierul

l = read_clasic()
print(l)

print('*'*40)

# Citire folosind Context Manager

def read_safe():
    with open("data.txt", "r") as f:
        return f.readlines()

l = read_safe()
print(l)
print('*'*40)

# Scriere date fisier
    # Suprascrie tot continutul anterior ( se pierd datele care au fost inainte )

def write():
    with open("data.txt", "w") as f:
        f.writelines(["1\n", " abc\n", " 1 2 3\n"])

write()

print('*'*40)

# Adaugare date in fisier

def append():
    with open("data.txt", "a") as f:
        f.writelines(["banane\n", "portocale\n"])

append()