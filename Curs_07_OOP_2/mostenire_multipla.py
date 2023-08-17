# class Car:
#     def go(self):
#         print('Vruuum, Vruuum')
#
#     def start(self):
#         print('Starting Car ')
#
#
# class Flyable:
#     def fly(self):
#         print("flu, flu")
#
#     def start(self):
#         print('starting flyable')
#
#
# class FlyngCar(Car, Flyable):
#         # Method Rezolution Order ( MRO ) -> regula dupa care se decide care este functie
#         # ce se apeleaza atunci cand avem o mostenire multipla, functii cu acelasi nume ( de la stanga la dreapta )
#     pass
#
#
# fc = FlyngCar()
# fc.fly()
# fc.go()
# fc.start()
#
#
# class FlyingCar2(Flyable, Car):
#     pass
#
#
# fc2 = FlyingCar2
# fc2.start()
class Car:
    def go(self):
        print("wrum, wrum")

    def start(self):
        print("starting car")


class Flyable:
    def fly(self):
        print("flu, flu")

    def start(self):
        print("starting flyable")

class FlyingCar(Car, Flyable):
    pass

fc = FlyingCar()
fc.fly()
fc.go()
fc.start()

""" Method resolution order ( MRO ) --> regula dupa care se decide care este functia 
ce se apeleaza atunci cand avem o mostenire multipla, functii cu acelasi nume
( de la stanga la dreapta ) """

class FlyingCar2(Flyable, Car):
    pass
fc2 = FlyingCar2()
fc2.start()