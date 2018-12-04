import numpy as np

puzzle = open('input.txt', 'r').readlines()

fabric = np.zeros((1000,1000))
val = []
for claim in puzzle:
    num = claim.split()[0]
    xsize, ysize = map(int, claim.strip().split()[3].split("x"))
    xpos, ypos  = map(int, claim.strip().split()[2].strip(":").split(","))
    fabric[xpos:xpos+xsize, ypos:ypos+ysize] += 1
    val.append((num, (xpos, ypos), (xsize, ysize)))

print("part one:", (fabric >= 2).sum())

for num, (xpos, ypos), (xsize,ysize) in val:
    if (fabric[xpos:xpos+xsize, ypos:ypos+ysize] == 1).all():
        print("part two:", num)
