# impired by https://www.redblobgames.com/grids/hexagons/#range 
data = open("./puzzle.txt","r").readline().strip().split(",")

x = 0
y = 0
z = 0
max_dist = 0

for direction in data:
    if direction == 'n':
        x -= 1
        z += 1
    elif direction == 'nw':
        x -= 1
        y += 1
    elif direction == 'ne':
        y -= 1
        z += 1
    elif direction == 'sw':
        y += 1
        z -= 1
    elif direction == 'se':
        x += 1
        y -= 1
    elif direction == 's':
        x += 1
        z -= 1
    dist = (max(abs(x),abs(y),abs(z)))
    if dist > max_dist:
        max_dist = dist
print("day11_1", dist)
print("day11_2", max_dist)

