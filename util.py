# A file with some common math operations.

from math import sqrt

def is_prime(num):
    if num % 2 == 0 and num > 2:
        return False
    for i in range(3, int(sqrt(num)) + 1, 2):
        if not num % i:
            return False
    return True

def proper_divisor_sum(num):
    div_sum = 0
    for i in range(1, num):
        if num % i == 0:
            div_sum += i
    return div_sum

