"""
Serializarea datelor --> se doreste persistarea datelor din aplicatie ptr a fi disponibilein viitor pentru
                         a putea fi citite sau modificate
"""


# Citire date in mod clasic
# se foloseste intotdeauna -try - except

def read_clasic():
    f = open("date.txt", "r")  # deschiderea fisierului si retinerea lui in variabila "f"
    try:
        return f.readlines()  # citim toate liniile din fisier
    except Exception as ex:
        print(f"Error: {ex}")
    finally:
        f.close()  # inchidem fisierul


l = read_clasic()
print(l)

print("--" * 30)


# Citire folosind ContextManager

def read_safe():
    with open("date.txt", "r") as f:
        return f.readlines()


l = read_safe()
print(l)

print("--" * 30)


# Scriere date in fisier
# suprascrie tot continutul anterior (se pierd datele care au fost inainte)
# datele nu se pot recupera (CTRL+Z in Pycharm pe fisier)

def write():
    with open("date.txt", "w") as f:
        f.writelines(["1\n", "abc\n", "1 2 3\n"])


write()

print("--" * 30)


# Adaugare date in fisier

def append():
    with open("date.txt", "a") as f:
        f.writelines(["banane\n"])


append()
