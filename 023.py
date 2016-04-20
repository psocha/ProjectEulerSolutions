"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

from util import *

def is_abundant_number(num):
    return proper_divisor_sum(num) > num

def is_sum2_possible(target, sorted_array):
    left = 0
    right = len(sorted_array) - 1
    while left <= right:
        sum2 = sorted_array[left] + sorted_array[right]
        if sum2 == target:
            return True
        elif sum2 < target:
            left += 1
        else:
            right -= 1
    return False

abundant_numbers = []
for i in range(1, 28124):
    if is_abundant_number(i):
        abundant_numbers.append(i)

unwritable_numbers = []
for i in range(1, 28124):
    if not is_sum2_possible(i, abundant_numbers):
        unwritable_numbers.append(i)

print(sum(unwritable_numbers))

