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

