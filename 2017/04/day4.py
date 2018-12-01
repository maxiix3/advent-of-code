import pandas as pd
lines = open("day4_puzzle.txt").readlines()
counter1 = 0
counter2 = 0
for line in lines:
    passfrase = line.split()
    if len(passfrase) == len(list(set(passfrase))):
        counter1 += 1
        sorted_passfrase = ["".join(sorted(x)) for x in passfrase]
        if len(list(set(sorted_passfrase))) == len(passfrase):
            counter2 +=1

print("day4_1", counter1)
print("day4_2", counter2)

