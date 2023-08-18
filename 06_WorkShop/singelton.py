# Se da următoarea clasa:


# class PresedinteRomania:
#     _instance = None
#     def __new__(cls):
#         '''
#         Metoda speciala __new__ este responsabila pentru crearea instantei obiectului
#         ......
#         '''
#         if cls._instance is None:
#             cls._instance = super(PresedinteRomania, cls).__new__(cls)
#             '''
#
#             '''
#             return cls._instance
#
#     def __str__(self):
#         return "Eu sunt presedintele Romaniei"
#
#     def say_hello(self):
#         return f'Salut! {self}'

# In momentul de fata, dacă încercăm să creăm mai multe obiecte din clasa aceasta, vom putea:
#
# a = PresedinteRomania()
# b = PresedinteRomania()
#
# print(f'ID(a) = {id(a)}')
# print(f'ID(b) = {id(b)}')
# print(f'Acelasi obiect? {a is b}')
'''
Acest pattern ne permite sa creăm un obiect dintr-o clasa folosind o alta clasa (fabrica). Fabrica are posibilitatea de a crea obiecte din mai multe clase (de obicei aceste clase sunt siblings, adica mostenesc de la acelasi parinte).

	
Vom implementa următoarele clase:
English/French/Spanish Translator – clase care știu sa traduca cuvinte din română în limba specificata
translations va fi un dicționar cu acele cuvinte, exemplu `{ “masina”: “car” }` – se poate hardcoda în clasa
localize va fi o funcție care pentru un parametru de intrare, ne va da traducerea lui în acea limba (exemplu `input(“masina”)` returneaza “car”)

TranslatorFactory – clasa care are o singura metoda (preferabil statica sau de clasa) numita get_translator(language) – in functie de parametrul language, returnează un translator object.


'''

print('*',40)
# class Fabrica:
#     def __init__(self, translations):
#         self.translations = translations
#     def localaize(self, word):
#         return self.translations.get(word, 'Translation not availabale')
# class EnglishTranslator(Fabrica):
#     def __init__(self):
#         super().__init__(
#             {
#                 'masina':'car',
#                 'barbat': 'man',
#                 'femeie':'woman',
#                 'copil':'child'
#             }
#         )
# class FranceTranslator(Fabrica):
#     def __init__(self):
#         super().__init__(
#             {
#                 'masina':'masina in franceza',
#                 'barbat': 'man in franceza',
#                 'femeie':'woman in franceza',
#                 'copil':'enfant'
#             }
#         )
# class SpanishTranslator(Fabrica):
#     def __init__(self):
#         super().__init__(
#             {
#                 'masina':'masina in sp',
#                 'barbat': 'man in sp',
#                 'femeie':'woman in spa',
#                 'copil':'enfant in sp'
#             }
#         )

# class TranslationFactory():
#     @classmethod
#     def get_translator(self, languege):
#         if languege == 'en':
#             return EnglishTranslator()
#         elif languege == 'fr':
#             return FranceTranslator()
#         elif languege == 'sp':
#             return SpanishTranslator()
#         else:
#             return ValueError('Invalid languege code')
# factory = TranslationFactory()
#
# english_trans = factory.get_translator('en')
# spanish_trans = factory.get_translator('es')
# spanish_trans = factory.get_translator('sp')
#
# print(f'In engleza zicem {english_trans.localize("masina")}')
# print(f'In spaniola zicem {spanish_trans.localize("masina")}')
#
# from abc import ABC, abstractmethod
# class TranslatorInterface(ABC):
#     @abstractmethod
#     @staticmethod
#     def localize(word):
#         pass
# class EnTranslator(TranslatorInterface):
#            traduceri ={
#                 'masina': 'car',
#                 'barbat': 'man',
#                 'femeie': 'woman',
#                 'copil': 'child'
#             }
#          @staticmethod
#         def localize(word):

