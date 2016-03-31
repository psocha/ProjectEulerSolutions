"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
3
7 4
2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom of the triangle below:
"""

triangle = []
maximum_sums = []
with open('input_files/018.txt') as f:
    lines = f.readlines()
    for line in lines:
        triangle.append([int(x) for x in line.split()])
        maximum_sums.append([0 for x in line.split()])

maximum_sums[0][0] = triangle[0][0]
for i in range(1, 15):
    for j in range(0, i + 1):
        if j == 0:
            maximum_sums[i][j] = triangle[i][j] + maximum_sums[i - 1][j]
        elif j == i:
            maximum_sums[i][j] = triangle[i][j] + maximum_sums[i - 1][j - 1]
        else:
            maximum_sums[i][j] = triangle[i][j] + max(maximum_sums[i - 1][j], maximum_sums[i - 1][j - 1])

max_bottom_row = 0
for i in range(15):
    max_bottom_row = max(maximum_sums[14][i], max_bottom_row)

print(max_bottom_row)

