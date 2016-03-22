"""
The following iterative sequence is defined for the set of positive integers:
    n -> n/2 if n is even
    n -> 3n + 1 if n is odd
Using the rule above and starting with 13, we generate the following sequence:
    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
"""

class CollatzCounter:
    def __init__(self):
        self.saved_lengths = {}

    def sequence_length(self, num):
        if num == 1:
            return 1
        else:
            collatz = self.next_collatz(num)
            if collatz in self.saved_lengths:
                result = 1 + self.saved_lengths[collatz]
            else:
                result = 1 + self.sequence_length(collatz)
            self.saved_lengths[num] = result
            return result

    def next_collatz(self, num):
        if num % 2 == 0:
            return num / 2
        else:
            return 3 * num + 1

    def print_map(self):
        print(sorted(self.saved_lengths.items(), key=lambda x: x[1]))

max_length = 0
max_index = 0
counter = CollatzCounter()
for i in range(1, 1000000):
    current_length = counter.sequence_length(i)
    if current_length > max_length:
        max_length = current_length
        max_index = i

print(max_index)

