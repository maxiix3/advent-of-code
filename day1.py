#### task

f = open('one.txt')
lines = f.readlines()
counter = 0
floor = 0
for line in lines:
    for i in range(len(line)):
        if line[i] == '(' :
            floor += 1
        elif line[i] == ')' :
            floor -= 1

print "floor = %d" %floor

#extra

f = open('one.txt')
lines = f.readlines()
counter = 0
floor = 0
for line in lines:
    for i in range(len(line)):
        if line[i] == '(' :
            floor += 1
            counter += 1
        elif line[i] == ')' :
            floor -= 1
            counter += 1

        if floor == -1:
            print "counter = %d" %counter
            break
