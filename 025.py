"""
The Fibonacci sequence is defined by the recurrence relation:
F(n) = F(n-1) + F(n-2), where F(1) = 1 and F(2) = 1.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

THRESHOLD = 10 ** 999

prevPrev = 1
prev = 1
result = 0
index = 2

while True:
    index += 1
    result = prev + prevPrev
    if result > THRESHOLD:
        break
    prevPrev = prev
    prev = result
    
print(index)

