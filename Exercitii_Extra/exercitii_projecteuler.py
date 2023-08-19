'''
If we list all the natural numbers below 10  that are multiples of 3 or 5 we get 3, 5, 6 and 9
. The sum of these multiples is 23
Find the sum of all the multiples of 3 or 5 below 1000.

'''
# def sum_of_multiples(limit):
#     total_sum = 0
#     for num in range(limit):
#         if num % 3 == 0 or num % 5 == 0:
#             total_sum += num
#     return total_sum
#
# limit = 1000
# result = sum_of_multiples(limit)
# print("The sum of all the multiples of 3 or 5 below", limit, "is:", result)
'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 
2-digit numbers is 9009=91*99.
Find the largest palindrome made from the product of two 3-digit numbers.

'''
def largest_palid(digiti):
    max_nr = 10**digiti - 1
    min_nr = 10**(digiti-1)
    l_palid = 0
    for n_max in range(max_nr, min_nr - 1, -1):
        for n_min in range (n_max, min_nr - 1, -1):
            rezultat = n_max * n_min

            if str(rezultat) == str(rezultat)[::-1] and rezultat > l_palid:
                l_palid = rezultat
    print(f'Cel mai mare palindrome a unui numar format din {digiti} este : {l_palid} si este rezultatul a {n_max} x {n_min}')
nr_dig = int(input('Introduceti un numar de digiti :'))
largest_palid(nr_dig)

# def is_palindrome(n):
#     return str(n) == str(n)[::-1]
#
# def largest_palindrome_product(digits):
#     max_num = 10**digits - 1
#     min_num = 10**(digits - 1)
#     largest_palindrome = 0
#
#     for num1 in range(max_num, min_num - 1, -1):
#         for num2 in range(num1, min_num - 1, -1):
#             product = num1 * num2
#             if product <= largest_palindrome:
#                 break
#             if is_palindrome(product) and product > largest_palindrome:
#                 largest_palindrome = product
#
#     return largest_palindrome
#
# num_of_digits = 8
# result = largest_palindrome_product(num_of_digits)
# print("The largest palindrome made from the product of two", num_of_digits, "-digit numbers is:", result)
