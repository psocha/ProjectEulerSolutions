"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
"""

singles = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
teens = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {10: 'ten', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

def num_letters(num):
    if num == 1000:
        return len('onethousand')

    letters = 0

    hundreds_digit = num // 100
    two_digits = num % 100
    if hundreds_digit > 0:
        letters = letters + len(singles[hundreds_digit] + 'hundred')
        if two_digits > 0:
            letters = letters + len('and')

    tens_digit = two_digits // 10
    ones_digit = two_digits % 10
    if tens_digit == 0:
        if ones_digit > 0:
            letters = letters + len(singles[ones_digit])
    elif tens_digit == 1:
        if ones_digit > 0:
            letters = letters + len(teens[10 * tens_digit + ones_digit])
        else:
            letters = letters + len(tens[10 * tens_digit])
    else:
        letters = letters + len(tens[tens_digit*10])
        if ones_digit > 0:
            letters = letters + len(singles[ones_digit])

    return letters

sum_letters = 0

for i in range(1, 1001):
    sum_letters = sum_letters + num_letters(i)

print(sum_letters)

