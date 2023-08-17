"""
Singleton -> design pattern care ne permite sa avem o clasa care returneaza mereu aceeasi instanta unica
          -> de obicei se foloseste in situatii in care nu ne intereseaza obiectul in sine ci doar
             anumite functionalitati ale acestuia

Avantaje: - poti fi sigura ca o clasa Singleton are o singura instanta
          - poti avea acces global catre aceasta instanta
          - obiectul Singleton este initializat doar o singura data (prima data cand este cerut)
Dezavantaje: - poate masca un design defectos de ex atunci cand componentele unui sistem stiu
               prea multe unele despre celelalte
"""


class SingletonLogger:
    _instance = None

    # functia __init__ in Python nu este un constructor traditional ci doar un initializator
    # inainte de __init__ este apelata functia __new__ unde se creeaza de fapt obiectul

    def __new__(cls, *args, **kwargs):
        # functia __new__ nu are "self" ca prim argument ptr ca "self" nu exista inca la momentul
        # rularii, in schimb avem cls care este o referinta catre clasa curenta

        if cls._instance is None:  # prima data cand este apelata Singletonlogger se creeaza obiectul
            print("creating_object")
            cls._instance = super().__new__(cls)
        return cls._instance  # returnam acelasi obiect de fiecare data


# logger = SingletonLogger()
# logger2 = SingletonLogger()
# print(logger, logger2)
# print(logger is logger2)

print("--" * 30)


class SingletonFileLogger(SingletonLogger):  # mostenirea facuta in acest fel, duce la problema
    # ca obiectul instantei Singleton poate fi de tipul SingletonLogger, nu SingletonFileLogger
    # daca el se creeaza inainte
    # ca si solutie vezi ex de mai jos cu SingletonLoggerMultiClass
    def __init__(self, file_name):
        self.file_name = file_name


sfl = SingletonFileLogger("Hello.txt")
sfl2 = SingletonFileLogger("Hello2.txt")
print(sfl, sfl2)
print(sfl.file_name, sfl2.file_name)

print("--" * 30)


class SingletonLoggerMultiClass:
    _instance = {}

    def __new__(cls, *args, **kwargs):
        if cls._instance.get(cls) is None: # verifica daca exista deja o instanta ptr clasa curenta
            # daca nu exista, o creeaza
            cls._instance[cls] = super().__new__(cls)
        return cls._instance[cls]

class SingletonFileLogger2(SingletonLoggerMultiClass):
    def __init__(self, file_name):
        self.file_name = file_name

l = SingletonLoggerMultiClass()
s = SingletonFileLogger2("Hello.txt")
l2 = SingletonLoggerMultiClass()
s2 = SingletonFileLogger2("Hello.txt")
print(l, l2)
print(s, s2)


