# A file with some common math operations.

from math import sqrt

def is_prime(num):
    if num % 2 == 0 and num > 2:
        return False
    for i in range(3, int(sqrt(num)) + 1, 2):
        if not num % i:
            return False
    return True

