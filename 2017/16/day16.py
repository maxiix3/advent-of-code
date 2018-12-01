from collections import deque

programs = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
f = open("./puzzle.txt").readline()
moves = f.strip().split(",")

def dance(programs):
    for move in moves:
        if move[0] == 's':
            n = int(move[1:])
            programs = deque(programs)
            programs.rotate(n)
            programs = list(programs)
        elif move[0] == 'x':
            a, b = map(int, move[1:].split('/'))
            programs[a], programs[b] = programs[b], programs[a]
        elif move[0] == 'p':
            a, b = map(programs.index, move[1:].split('/'))
            programs[a], programs[b] = programs[b], programs[a]
    return programs

print("day16_2:", dance(programs))

i = 0
while i < 1000000000:
    programs = dance(programs)
    i += 1
    if programs == ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']:
        i = 1000000000 - (1000000000 % i)
print("day16_2:", programs)

