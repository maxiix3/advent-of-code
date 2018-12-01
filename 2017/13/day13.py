import itertools
firewalls = open("./puzzle.txt").readlines()

firewall = {}
part1 =  0
counter = 0

for line in firewalls:
    a, b = line.strip().split(":")
    firewall[int(a)] = int(b)


def scan(size, moves):
    offset = moves % ((size - 1) * 2)
    if offset > size-1:
        return 2 * (size -1) - offset
    else:
        return offset

for pos in firewall:
    if scan(firewall[pos], pos) == 0:
        part1 += pos * firewall[pos]

print("day13_1:", part1)

for delay in range(10**9):
    trough = True
    for pos in firewall:
        if scan(firewall[pos],(pos+delay)) == 0:
            trough = False
            break
    if trough:
        print("day13_2:", delay)
        break


