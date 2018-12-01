f = open("./puzzle.txt", "r").readlines()
group = []
pipes = {}

for line in f:
    x, y = line.strip().split("<->")
    pipes[int(x)] = eval('[' + y + ']')

def find_pipes(p):
    if p in group:
        return []
    else:
        group.append(p)
    for i in pipes[p] + [p]:
        res = find_pipes(i)
    return res

find_pipes(0)
print("day12_1:", len(group))

groups = []
for p in pipes:
    group = []
    find_pipes(p)
    groups.append(sorted(group))

groups = set(tuple(x) for x in groups)
groups = [ list(x) for x in groups]

print("day12_2:", len(groups))
