# # def - functie
# def printGreeting():
#     print('Buna ziua! Bine ati venit')
# def printGreetingByName(nume, prenume):
#     print(f'Buna ziua {nume} {prenume}')
# def mediaNr(a, b, c):
#     return ((a+b+c)/3)
# def piValue():
#     return 3.14
#
# # exercitiu
# # daca persoana este majora, altfel fals
# def verificareMajor(varsta):
#     if varsta >= 18:
#         return True
#     else:
#         return False
#
#
# # zona apelare
# printGreeting()
# printGreeting()
# printGreetingByName('Holom', 'Adrian')
# print(mediaNr(3,3,4))
# print(piValue())
#
# print(verificareMajor(17))
#
# # se ia varsta utilizatorului
# age = int(input('Introduceti varsta dumneavoastra ... '))
# if verificareMajor(age):
#     print('Cont creat bine ai venit in aplicatie')
# else:
#     print('Nu ai varsta minima necesara pentru a paria!!!')
#
# # OOP
# # variabile => atribute, proprietati sau fields
# # functii => metode

# jucatori = ['Jucator1', 'Jucator2', 'Jucator3', 'Jucator4', 'Jucator5'] # lista cu jucatori
# schimbari_efectuate = 0
# schimbari_max = 3
#
# jucator_in = 'Jucator6' # cel care intra
# jucator_out = 'Jucator3' # cel care iese
#
# if jucator_out in jucatori: # verifica daca jucatorul  are iese este in lista
#     jucatori.remove(jucator_out) # sterge jucatorul existent din lista
#     jucatori.append(jucator_in) # il adauga pe cel nou
#     schimbari_efectuate += 1 # incrementeaza schimbarile
#     print(f"A intrat {jucator_in}, a iesit {jucator_out}, mai ai {schimbari_max - schimbari_efectuate} schimbari.")
# else:
#     print(f"Nu se poate efectua schimbarea deoarece jucatorul {jucator_in} nu este in teren. Mai ai {schimbari_max - schimbari_efectuate} schimbari.")
# # mai sus ne ramane 2 schimbari
# # Rulam in acelasi script cu alti jucatori dupa acelasi model
# jucator_in = 'Jucator7'
# jucator_out = 'Jucator2'

# x = int(input("Introduceti un numar natural x: "))
#
# p = 1
# m = -1
#
# while p <= x:
#     c = (x // p) % 10  # Se obține cifra curentă în baza 10
#     if c > m:
#         m = c
#         p *= 10
#     else:
#         x = (x // (p * 10)) * p + x % p
#
# if m >= 0:
#     print(x)
# else:
#     print("nu")

# n = int(input('Introduceti lungimea sirului : '))
# s = int(input("Introduceti "))
# class Solution:
#     def subArraySum(self, arr, n, s):
#         a1 = 0
#         a2 = 0
#         result = 0
#         if s == 0:
#             return [-1]
#         while a1 < n:
#             result += arr[a1]
#             while result > s:
#                 result -= arr[a2]
#                 a2 += 1
#             if result == s:
#                 return [a2 + 1, a1 + 1]
#             a1 += 1
#         if result != s:
#             return [-1]
#
#
# solutie = Solution()
#
# print(solutie.subArraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 20))

# class Solution:
#     def missingNumber(self,array,n):
#         self.array = array
#         self.n = n
#         suma_n = self.n * (self.n+1) // 2
#         suma_array = sum(self.array)
#         lipsa = suma_n - suma_array
#         return lipsa
# a = Solution()
# print(a.missingNumber([1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, ], 10))

# class Solution:
#     def duplicates(self, arr, n):
#         self.arr = arr
#         self.n = n
#         rezultat = []
#
#         for i in range(self.n):
#             index = abs(self.arr[i])
#
#             if self.arr[index] >= 0:
#                 self.arr[index] = -self.arr[index]
#             else:
#                 rezultat.append(index)
#         if len(rezultat) == 0:
#              return [-1]
#
#         rezultat.sort()
#         return rezultat
#
#
# p = Solution()
# print(p.duplicates([0, 3, 3, 2, 3, 1, 3, 1, 2, 4, 3, 3, 3], 5))
