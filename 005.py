"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?)
"""

from util import *

def product_of_common_primes(num):
    product = 1
    for x in range(2, num + 1):
        if is_prime(x):
            product = product * x
    return product

smallest = 0
counter = 0

interval = product_of_common_primes(20)

while smallest == 0:
    counter = counter + interval
    for x in range(20, 0, -1):
        if counter % x:
            break
        if x == 1:
            smallest = counter

print(smallest)

