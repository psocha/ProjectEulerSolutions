"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""

from util import *

def largest_prime_factor(num):
    if is_prime(num):
        return num
    for i in range(int(sqrt(num)), 1, -1):
        if is_prime(i) and not num % i:
            return i

print(largest_prime_factor(600851475143))

