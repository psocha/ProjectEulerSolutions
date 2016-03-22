"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""

total = 0
with open('input_files/013.txt') as f:
    lines = f.readlines()
    for line in lines:
        if int(line) > 0:
            total = total + int(line)

print(str(total)[0:10])

