f = open("./day5_puzzle.txt", "r").readlines()
l1 = []
l2 = []
for line in f:
    l1.append(int(line))
    l2.append(int(line))
counter1 = 0
pos = 0
while pos < len(l1):
    tmp = l1[pos]
    l1[pos] += 1
    pos += tmp
    counter1 += 1
print("day5_1 ", counter1)

counter2 = 0
pos = 0
while pos < len(l2):
    tmp = l2[pos]
    if tmp < 3:
        l2[pos] += 1
    else:
        l2[pos] -= 1
    pos += tmp
    counter2 += 1
print("day5_1", counter2)
