#!/usr/bin/env python

puzzle = open('./day1_puzzle.txt', 'r').readline()
length = len(puzzle)
day1_1 = 0
for i in range(length-1):
    if puzzle[i] == puzzle[i+1]:
        day1_1 += int(puzzle[i])
if puzzle[0] == puzzle[-2]:   # new line char is -1
    day1_1 += int(puzzle[0])
print("day1_1", day1_1)

length = int(len(puzzle)/2)
day1_2 = 0
for i in range(length):
    if puzzle[i] == puzzle[length+i]:
        day1_2 += int(puzzle[i])*2
print("day1_2", day1_2)
