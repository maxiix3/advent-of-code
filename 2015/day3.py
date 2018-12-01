f = open("day3.txt")
lines = f.readlines()
x=0
y=0
unique= 0
grid = {}
grid[x,y] = 1
for line in lines:
    for i in range(len(line)):
        if line[i] == 'v':
            y -= 1
        elif line[i] == '^':
            y += 1
        elif line[i] == '<':
            x -= 1
        elif line[i] == '>':
            x += 1
        grid[x,y] = 1
    for i in grid:
        unique += 1
print "Only Santa = %d " %unique

#extra
f = open("day3.txt")
lines = f.readlines()
x=0
y=0
robox=roboy=0
unique= 0
grid = {}
grid[x,y] = 1
robo = False
for line in lines:
    for i in range(len(line)):
        if robo == False:
            if line[i] == 'v':
                y -= 1
                robo = True
            elif line[i] == '^':
                y += 1
                robo = True
            elif line[i] == '<':
                x -= 1
                robo = True
            elif line[i] == '>':
                x += 1
                robo = True

            grid[x,y] = 1
 
        elif robo == True:
            if line[i] == 'v':
                roboy -= 1
                robo = False
            elif line[i] == '^':
                roboy += 1
                robo = False
            elif line[i] == '<':
                robox -= 1
                robo = False
            elif line[i] == '>':
                robox += 1
                robo = False

            grid[robox,roboy] = 1

    for i in grid:
        unique += 1
print "with robo-santa and santa = %d" %unique



