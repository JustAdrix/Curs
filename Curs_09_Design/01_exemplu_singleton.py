'''Singelton -> design pattern care ne permite sa avem o clasa care returneaza mereu aceasi instanta unica
                de obicei se foloseste in situati in care nu ne intereseaza obiectul in sine ci daor anumite
                 functionalitati ale acestuia
Avantaje :
            Poti fi sigur ca o clasa Singleton are o singura instanta
            Poti avea acces global catre aceiasi instanta
            Obiectul Singleton este initializat doar o singura data ( prima data cand este cerut)
Dezavantaje:
            Poate masca un design defectuos ex. atunci cand componentele unui sistem stiu pre multe unele despre
            celalalte


'''


class SingletonLogger:
    _instance = None

    # functia __init__ in Python nu este un constructor traditional ci doar un initializator
    # ininte de __init__ este apelata functia __new__ unde se creaza de fapt obiectul
    def __new__(cls, *args, **kwargs):
        ''' functia __new__ nu are self ca prim argument pentru ca self nu exista inca la momentul rulari
        in schimb avem cls care este o referinta catre clasa curenta'''
        if cls._instance is None:  # prima data cand este apelat SingeletonLoggger se creaza obiectul
            print('Creating object')
            cls._instance = super().__new__(cls)
        return cls._instance  # returneaza acelasi obiect de fiecare data


# logger = SingletonLogger()
# logger2 = SingletonLogger()
# print(logger, logger2)
# print(logger is logger2)

print("*" * 30)


class SingeletonFileLogger(SingletonLogger):  # mostenirea facuta in acest fel duce la problema ca obiectul instantei
    # Singelton poate fi de tipul SinfeltonLogger, nu SingeltonFileLogger daca el se creaza ininte
    def __init__(self, file_name):
        self.file_name = file_name


sfl = SingeletonFileLogger('Heloo.txt')
sfl2 = SingeletonFileLogger('Hello2.txt')
print(sfl, sfl2)
print(sfl.file_name, sfl2.file_name)


class SingletonLoggerMultiClass:
    _instance = {}

    def __new__(cls, *args, **kwargs):
        if cls._instance.get(cls) is None:  # verifica daca exista o instanta pentru clasa curenta daca nu o creazs
            cls._instance[cls] = super().__new__(cls)
        return cls._instance[cls]


class SingletonFileLogger2(SingletonLoggerMultiClass):
    def __init__(self, file_name):
        self.file_name = file_name


l = SingletonLoggerMultiClass()
s = SingletonFileLogger2("Hello.txt")
l2 = SingletonLoggerMultiClass()
s2 = SingletonFileLogger2('Hello.txt')
print(l, l2)
print(s, s2)

