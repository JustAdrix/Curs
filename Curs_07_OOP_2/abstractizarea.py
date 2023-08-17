# se defineste o clasa care nu poate exista de sine statatoare
# forteaza anuminte comportamente pentru a putea defini clasa
# 0 clasa abstracta este o clasa care cel putin o clasa abstracta

from abc import ABC, abstractmethod  # abc - abstract base class


class Animal(ABC):  # clasele trebuie sa mosteneasca din ABC
    @abstractmethod
    def sound(self):
        pass

    # functiile abstracte sunt functii fara implementare
    @abstractmethod
    def sleep(self):
        raise NotImplementedError


class Dogg(Animal):
    def sound(self):
        print('woph')
    def sleep(self):
        print('zzzzz')
class Cat(Animal):
    def sound(self):
        print('miau')

    def sleep(self):
        print('rrrr')

'''
a = Animal() # Eroare deoarece nu se pot instantia clase abstracte
a,sleep()
'''

