"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

from util import *

prime_sum = 2
for i in range(3, 2000000, 2):
    if is_prime(i):
        prime_sum = prime_sum + i

print(prime_sum)

