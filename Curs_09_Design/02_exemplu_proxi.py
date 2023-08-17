'''
Proxi este un sablon structural care te lasa sa dai un substitut penreu un alt obiect
Un obiect proxi controleaza accesul catre obiectul original lasand doar anumite operatii sa fie efectuate sau sa adauge
pasi extra ininte sau dupa operatia in sine
Avantaje :
        Poti controla obiectul real fara ca cineva sa stie ca il utilizezi
        POTI CONTROLA ciclul de viata al obiectului real cand cei care il utilizeaza nu la pasa despre asta
        Functioneaza chiar daca obiectul real nu este pregatit sau nu este disponibil
DEZAVANTAJE:
        cODUL DEVINE MAI COMPLICAT DEOARECE ESTE NECESARA   INTRODUCEREA mai multor clase
        Rezultatul obtinut de la obiectul real poate fi intarziat, neavand acces direct la acesta

'''

from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def request(self):
        print("Real Subject: handling request")
class Proxy(Subject):
    def _init__(self, real_request):
        self.real_request = real_request
    def check_acces(self):
        print(' Proxy: Checking acces before real request')
        return True
    def request(self):
        if self.check_acces():
            self.real_request.request()
rs = RealSubject()
p = Proxy(rs)
p.request()
