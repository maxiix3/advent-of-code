IDs=open('puzzle.txt','r').read().strip().split()

two=0
three=0
for ID in IDs:
    if any(ID.count(c) == 2 for c in set(ID)):
        two+=1
    if any(ID.count(c) == 3 for c in set(ID)):
        three+=1

print("part one:", two*three)

for i in IDs:
    for j in IDs:
        diff = 0
        for pos, char in enumerate(i):
            if char != j[pos]:
                diff +=1
        if diff == 1:
            ans = [char for pos, char in enumerate(i) if j[pos] == char]
            print("Part Two:", ''.join(ans))


