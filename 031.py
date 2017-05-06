"""
In England the currency is made up of pound, $, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, $1 (100p) and $2 (200p).
It is possible to make $2 in the following way:

1*$1 + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p
How many different ways can $2 be made using any number of coins?
"""

coins = [200, 100, 50, 20, 10, 5, 2, 1]

def num_combinations(amount, starting_index):
    if amount < 0:
        return 0
    elif amount == 0:
        return 1
    elif starting_index == 7:
        return 1
    else:
        return num_combinations(amount - coins[starting_index], starting_index) \
            + num_combinations(amount, starting_index + 1)

print(num_combinations(200, 0))
