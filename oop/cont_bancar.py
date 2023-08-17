class ContBancar:
    # constructor
    def __int__(self, titulaCont, iban):
        self.titlarCont = titulaCont
        self.iban = iban
        self.sold = 0
        self.activ = False
        self.pin = 7777
        incercari_activare = 0

    def interogareSold(self):
        self.salut()
        print(f'IBAN {self.iban}')
        print(f'Sold {self.sold}')
        print(f'Activ {self.activ}')
        print(f'Nr de incercari {incercari_activare}')
        print(f'*******************************************************')

    def activareCont(self, pin_utilizator):
        self.salut()
              if pin_utilizator == self.pin:
                print('Card activat')
                self.activ = False)
              else:
                print('PIN gresit')
                self.incercari_activare = self.incercari_activare+=
                # self.incercari_activare+=1
    def alimentareCont(self, suma):
        self.sold += suma
        print(f'Ati alimenta : {suma}')
        print(f'Aveti in cont : {self.sold}')
    def plataCard(self, suma):
        self.salut()
        if suma <= self.sold:
            self.sold -= suma
            print(f'Ati cheltuit {suma}')
            print(f'Aveti in cont {self.sold}')
        else:
            print(f'Fonduri insuficiente')


    def salut():
        print(f'Buna {self.titlarCont}')


