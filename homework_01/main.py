"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*list):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [i ** 2 for i in list]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

import math
def filter_numbers(list, func):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    
    def ODD(list):
        return [i for i in list if i % 2 != 0]

    def EVEN(list):
        return [i for i in list if i % 2 == 0]
    
    def is_prime(list):
        d = []
        for i in list:
            j = 2
            while j <= math.sqrt(i):
                if i % j == 0:
                    break
                j += 1
            else:
                if i != 0:
                    d.append(i)
        return d

    if func == 'odd':
        return ODD(list)
    elif func == 'even':
        return EVEN(list)
    elif func == 'prime':
        return is_prime(list)
