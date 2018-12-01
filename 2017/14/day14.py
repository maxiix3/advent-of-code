import sys
from collections import Counter
sys.path.append('../10')
from day10 import knot_hash
sys.setrecursionlimit(1500000)

#key = "ffayrhll"
key = "flqrgnkx"
grid = [[0 for x in range(128)] for y in range(128)] 

for i in range(128):
    tmp = key + "-" + str(i)
    res = knot_hash(tmp)
    column = format((int(res, 16)),'0128b')
    for j in range(128):
        grid[i][j] = column[j]

su = 0
for i in range(128):
    for j in range(128):
        if grid[i][j] == '1': su += 1
print("day14_1:", su)

used = []
counter = 0

def has_neighbours(i,j, root):
    global counter
    if [i,j] in used:
        return -1
    else:
        used.append([i,j])
    if grid[i][j] != '1':
        return -1
    if root == True:
        counter += 1
    if i > 0:
        has_neighbours(i-1, j, False)
    if j > 0:
        has_neighbours(i, j-1, False)
    if i < 127:
        has_neighbours(i+1, j, False)
    if j < 127:
        has_neighbours(i, j+1, False)

for i in range(128):
    for j in range(128):
        has_neighbours(i,j,True)

print("day14_2:", counter)
