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
n = 384

arr = '887 778 916 794 336 387 493 650 422 363 28 691 60 764 927 541 427 173 737 212 369 568 430 783 531 863 124 68 136 930 803 23 59 70 168 394 457 12 43 230 374 422 920 785 538 199 325 316 371 414 527 92 981 957 874 863 171 997 282 306 926 85 328 337 506 847 730 314 858 125 896 583 546 815 368 435 365 44 751 88 809 277 179 789 585 404 652 755 400 933 61 677 369 740 13 227 587 95 540 796 571 435 379 468 602 98 903 318 493 653 757 302 281 287 442 866 690 445 620 441 730 32 118 98 772 482 676 710 928 568 857 498 354 587 966 307 684 220 625 529 872 733 830 504 20 271 369 709 716 341 150 797 724 619 246 847 452 922 556 380 489 765 229 842 351 194 501 35 765 125 915 988 857 744 492 228 366 860 937 433 552 438 229 276 408 475 122 859 396 30 238 236 794 819 429 144 12 929 530 777 405 444 764 614 539 607 841 905 819 129 689 370 918 918 997 325 744 471 184 491 500 773 726 645 591 506 140 955 787 670 83 543 465 198 508 356 805 349 612 623 829 300 344 747 569 341 423 312 811 606 802 662 731 879 306 321 737 445 627 523 466 709 417 283 259 925 638 63 625 601 37 453 900 380 551 469 72 974 132 882 931 934 895 661 164 200 982 900 997 960 774 814 669 191 96 927 467 85 341 91 685 377 543 937 108 446 757 180 419 888 413 349 173 660 10 337 211 343 588 207 302 714 373 322 256 820 600 722 905 940 812 941 668 706 229 128 151 985 659 921 225 423 270 397 82 631 85 293 973 673 851 626 386 223 300 641 43 899 714 299 191 525 591 210 582 820 337 733 156 995 5 380 770 274 777 851 256 861 143 580 885 994 206 622'

#print(arr[:,[len(arr)-1],2].)
def printNos(N):
    if N > 0:
        printNos(N - 1)
        print(N, end=" ")

# Example 1
N1 = 10
printNos(N1)  # Output: 1 2 3 4 5 6 7 8 9 10

print()  # Newline

# Example 2
N2 = 5
printNos(N2)  # Output: 1 2 3 4 5