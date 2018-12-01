import numpy as np

def downright(n):
    return (2*n+1)**2

inp = int(open("./day3_puzzle.txt").readline())
for i in range(10000):
    if downright(i) >= int(inp):
        downright_num = downright(i)
        break

downright_dist = np.sqrt(downright_num)-1
colum = downright_dist/2
downleft_num =  downright_num - colum
upleft_num = downleft_num - colum
row_index = -colum
if inp < downleft_num:
    if upleft_num < inp:
        print("day3_1 ", row_index - (inp-upleft_num) + colum)
    else:
        print("day3_1 ", row_index + (upleft_num-inp) + colum)
else:
    print("day3_1 ", abs(row_index + (downright_num-inp)) + colum)


x = y = dx = 0
dy = -1
coords = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
grid = {}

while True:
    total = 0
    for offset in coords:
        ox, oy = offset
        if (x+ox, y+oy) in grid:
            total += grid[(x+ox, y+oy)]
    if total > inp:
        print("day3_2 ", total)
        break
    if (x, y) == (0, 0):
        grid[(0, 0)] = 1
    else:
        grid[(x, y)] = total
    if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1-y):
        dx, dy = -dy, dx
    x, y = x+dx, y+dy

