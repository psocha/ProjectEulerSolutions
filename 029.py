"""
Consider all integer combinations of a^b for 2 <= a <= 5 and 2 <= b <= 5:

2^2=4, 2^3=8, 2^4=16, 2^5=32
3^2=9, 3^3=27, 3^4=81, 3^5=243
4^2=16, 4^3=64, 4^4=256, 4^5=1024
5^2=25, 5^3=125, 5^4=625, 5^5=3125
If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

How many distinct terms are in the sequence generated by a^b for 2 <= a <= 100 and 2 <= b <= 100?
"""

def prime_factorization_of_power(a, b):
    base_prime_factors = prime_factorization(a)
    power_prime_factors = []
    for factor in base_prime_factors:
        power_prime_factors.extend([factor] * b)
    return power_prime_factors


def prime_factorization(n):
    prime_factors = []
    current = n
    d = 2
    while current > 1:
        if current % d != 0:
            d += 1
            continue
        prime_factors.append(d)
        current /= d
    return prime_factors


factorizations_found = set()
for a in range(2, 100 + 1):
    for b in range(2, 100 + 1):
        factorization = prime_factorization_of_power(a, b)
        factorizations_found.add(tuple(factorization))
print(len(factorizations_found))