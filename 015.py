"""
Starting in the top left corner of a 2*2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20*20 grid?
"""

lattice = [[0]*21 for i in range(21)]

for i in range(21):
    lattice[0][i] = 1
    lattice[i][0] = 1

for i in range(1, 21):
    for j in range(1, 21):
        lattice[i][j] = lattice[i-1][j] + lattice[i][j-1]

print(lattice[20][20])

