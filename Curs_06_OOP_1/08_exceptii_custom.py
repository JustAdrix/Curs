class CustomException(Exception):
    pass


"""
Sa se scrie o functiie care verifica daca o lista de numere intregi primite ca 
parametru contine numere negative.
Daca da sa se arunce o exceptie specifica.
"""


class ContainsNegativeNumbersException(Exception):
    pass


def verify_negative_numbers(numbers):
    for num in numbers:
        if num < 0:
            raise ContainsNegativeNumbersException(f"Contine {num}")


verify_negative_numbers([2, 5, -4, 6, -2])
