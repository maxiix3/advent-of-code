grid = {}

def ins(x,y):
    try:
        grid[x,y] += 1
    except KeyError:
        grid[x,y] = 1
    if grid[x,y] == 2:
        print abs(x)+abs(y)

def day1():
    f = open("day1.txt")
    lines = f.readlines()
    x=0
    y=0
    grid[x,y] = 1
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
                for i in range(y+1,y+a):
                    ins(x,i)
                y += a
            elif dirnum == 1: # East
                for i in range(x+1,x+a):
                    ins(i,y)
                x += a
            elif dirnum == 2: # South
                for i in range(y-1,y-a,-1):
                    ins(x,i)
                y -= a
            elif dirnum == 3: # West
                for i in range(x-1,x-a,-1):
                    ins(i,y)
                x -= a
    return x,y

day1()

