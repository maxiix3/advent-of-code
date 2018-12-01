def day1():
    f = open("day1.txt")
    lines = f.readlines()
    x=0
    y=0
    dirnum = 0
    for line in lines:
        splitted = line.split(", ")
        for i in splitted:
            if i[0] == "R":
                dirnum += 1
                if dirnum == 4:
                    dirnum = 0
            elif i[0] == "L":
                dirnum -= 1
                if dirnum == -1:
                    dirnum = 3
            a = int(i[1:])
            if dirnum == 0:  # North
                y += a
            elif dirnum == 1: # East
                x += a
            elif dirnum == 2: # South
                y -= a
            elif dirnum == 3: # West
                x -= a
    return x,y
x,y = day1()

print abs(x)+abs(y)
