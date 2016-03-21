"""
In the 20*20 grid below, four numbers along a diagonal line have been marked in red.
The product of these numbers is 26 * 63 * 78 * 14 = 1788696.
What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20*20 grid?
"""

grid = []
with open('input_files/011.txt') as f:
    lines = f.readlines()
    for line in lines:
        grid.append([int(x) for x in line.split()])

max_product = 0

for i in range(0, 17):
    for j in range(0, 20):
        max_product = max(grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j], max_product)

for i in range(0, 20):
    for j in range(0, 17):
        max_product = max(grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3], max_product)

for i in range(0, 17):
    for j in range(0, 17):
        max_product = max(grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3], max_product)

for i in range(3, 20):
    for j in range(0, 17):
        max_product = max(grid[i][j] * grid[i-1][j+1] * grid[i-2][j+2] * grid[i-3][j+3], max_product)

print(max_product)

