"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def find_abc():
    for c in range(1, 999):
        for a in range(1, c):
            b = 1000 - a - c
            if a**2 + b**2 == c**2:
                return a * b * c

print(find_abc())

