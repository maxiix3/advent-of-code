#!/usr/bin/env python

f = open("puzzle.txt")
lines = f.readlines()

def sum_in_list1(n,m):
    if (n+m == 2020):
        return n*m
    return -1

def part1():
    for i in range(len(lines)):
        for j in range(len(lines)):
            if (sum_in_list1(int(lines[i]),int(lines[j])) != -1):
                return "answer part 1: %d" % sum_in_list1(int(lines[i]),int(lines[j]))

def sum_in_list2(n,m,o):
    if (n+m+o == 2020):
        return n*m*o
    return -1

def part2():
    for i in range(len(lines)):
        for j in range(len(lines)):
            for k in range(len(lines)):
                if (sum_in_list2(int(lines[i]),int(lines[j]),int(lines[k])) != -1):
                    return "answer part 2: %d" % sum_in_list2(int(lines[i]),int(lines[j]),int(lines[k]))

print (part1())
print (part2())
