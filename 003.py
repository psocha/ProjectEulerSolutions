from math import sqrt

def is_prime(num):
    if num % 2 == 0 and num > 2:
        return False
    for i in range(3, int(sqrt(num)) + 1, 2):
        if not num % i:
            return False
    return True

def largest_prime_factor(num):
    if is_prime(num):
        return num
    for i in range(int(sqrt(num)), 1, -1):
        if is_prime(i) and not num % i:
            return i

print(largest_prime_factor(600851475143))

