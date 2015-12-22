import itertools as it

puzzle = '1113222113'
# for part2 change 40 to 50
for i in range(40):
    new_puzzle = []
    for k, g in it.groupby(puzzle):
        new_puzzle.append(str(len(list(g))))
        new_puzzle.append(k)
    puzzle = "".join(new_puzzle)

print len(puzzle)
