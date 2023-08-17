'''
Observer este un sablon de proiectare comportamental care te lasa sa definesti un mecanism de subscriere prin care

'''

from abc import ABC, abstractmethod
class Observer(ABC):
    @abstractmethod
    def update(self, obsarvable):
        pass
class Observable(ABC):
    @abstractmethod
    def register_observer(self,observer):
        pass
    @abstractmethod
    def notify(self):
        pass
class Subject(Observable):
    _observers = []
    def __init__(self, message):
        self.message = message
    def register_observer(self,observer):
        self._observer.append(observer)
    def notify(self):
        for ob in self._observers:
            ob.update(self)
    @property
    def message(self):
        return self.__message
    @message.setter
    def message(self, value):
        self.__message = value
        self.notify()
class RealObserverA(Observer):
    def update(self, obsarvable):
        if obsarvable.message.startswich('a'):
            print('Observator A notificat')
class RealObserverB(Observer):
    def update(self, obsarvable):
        if obsarvable.message.startswich('b'):
            print('Observator B notificat')
a = RealObserverA()
b = RealObserverB()

from dataclasses import dataclass
@dataclass
class Person(Observer):
    name: str
    def send_message(self,chat_room):
        message = input(f'{self.name} introdu un mesaj: ')
        chat_room.add_message(Message(self.name, message))
    def update(self, observable):
        if observable.istoric[-1].content.startswith(self.name):
            print(f'{self.name} ai primit un mesaj nou')
            response = input('Vrei sa raspunzi ? ( Y/N)')
            if response == 'y':
                self.send_message(observable)

@dataclass
class Message:
    autor: str
    content: str
class ChatRoom(Observable):
    _observers = []

    def __init__(self):
        self.istoric = []

    def notify(self):
        for ob in self._observers:
            ob.update(self)

    def register_observer(self, observer):
        self._observers.append(observer)

    def add_message(self, message):
        self.istoric.append(message)
        self.notify()
chat = ChatRoom()
s = Person("Sergiu")
v = Person("Valentin")
c = Person("Carmen")
chat.register_observer(s)
chat.register_observer(v)
chat.register_observer(c)
s.send_message(chat)