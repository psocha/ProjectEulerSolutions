"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

def is_pandigital(concat_str):
    if '0' in concat_str:
        return False
    non_duplicates = ''.join(set(concat_str))
    return len(non_duplicates) == 9

pandigitals = set()

# The smaller number can never be 3 digits or longer.
# 3 digits * 3 digits = 5+ digits, which adds up to 11+ digits.
# 98 is the highest 2-digit number with non-duplicate digits.
for i in range(1, 99):
    # The larger number can never be 5 digits or longer.
    # 1 digit * 5 digits = 5+ digits, which adds up to 11+ digits.
    # 9876 is the highest 4-digit number with non-duplicate digits.
    for j in range(i + 1, 9877):
        product = i * j
        concat_str = str(i) + str(j) + str(product)
        if len(concat_str) > 9:
            break
        if is_pandigital(concat_str):
            pandigitals.add(product)

print(sum(pandigitals))
