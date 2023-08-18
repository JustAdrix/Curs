def requre_login(method):
    def wrapper(self, *args, **kwargs):
        if not self.logedin:
            print('Acces nepermis, utilizatorul nu este logat !!!')
            return
        return method(self, *args, **kwargs)

    return wrapper


class User:
    def __init__(self, nume, email, parola, data_nasterii):
        self.nume = nume
        self.email = email
        self.parola = parola
        self.data_nasterii = data_nasterii
        self.logedin = False

    def login(self, email, parola):
        if self.email == email and self.parola == parola:
            self.logedin = True
            print('Utilizatorul sa logat cu succes!!!')
        else:
            print('Email sau Parola incorecte !!!')

    @requre_login
    def get_info(self):
        return {
            'nume': self.nume,
            'email': self.email,
            'data nasterii': self.data_nasterii
        }

    def logout(self):
        if self.logedin:
            self.logedin = False  # resetam starea de autentificare
            print('Utilizatorul a fost delogat !!!')
        else:
            print('Utilizatorul nu este logat !!!')


user = User('Ion', 'ion@itfactory.ro', 'parola', '03.06.20')
print(user.get_info())
user.login('ion@itfactory.ro', 'parola')
print(user.get_info())
user.logout()
print(user.get_info())
user.login('ion@itfactory.ro', 'parola')
print(user.get_info())
