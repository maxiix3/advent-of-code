step = 324
pos = 0
l = [0]

for i in range(1,2018):
    pos = ((pos + step) % len(l)) +1
    l.insert(pos, i)

print("day17_1:", l[l.index(2017)+1])

pos = 0
value = 0

for i in range(1,50000001):
    pos = ((pos + step)%i) +1
    if pos == 1:
        value = i

print("day17_2:", value)
