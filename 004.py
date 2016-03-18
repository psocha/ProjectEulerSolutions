"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(num):
    return str(num) == str(num)[::-1]

largest = 0
for x in range(100, 1000):
    for y in range(100, 1000):
        product = x * y
        if is_palindrome(product) and product > largest:
            largest = product

print(largest)

