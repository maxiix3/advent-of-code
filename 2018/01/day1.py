#!/usr/bin/env python

puzzle = open('./day1_puzzle.txt', 'r').readlines()
def day1(once):
    i = 0
    seen = [0]
    while True:
        for line in puzzle:
            i += int(line)
            if i not in seen:
                seen.append(i)
            else:
                return i
        if once:
            return i

print("Day1_1 = " ,day1(True))
print("Day1_2 = " ,day1(False))

