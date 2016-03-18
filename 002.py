
"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

sum = 0
a = 1
b = 1
fib = a + b

while fib < 4000000:
    if fib % 2 == 0:
        sum = sum + fib
    a = b
    b = fib
    fib = a + b

print(sum)

