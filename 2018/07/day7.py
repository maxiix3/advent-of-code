import re
import numpy as np
from collections import defaultdict
import string
puzzle = sorted(open('input.txt').readlines())

req_dict = defaultdict(set)
for line in puzzle:
    m = re.findall(r'Step (.) must be finished before step (.) can begin.', line)[0]
    req_dict[m[1]].add(m[0])
    s = [chr(i) for i in range(65,91)]
    a = set()
for i in range(100):
    for j in s:
        if j not in a and req_dict[j] & a == req_dict[j]:
            print(j, end='')
            a.add(j)
            break



#################################################
"""
old_list = []
new_list = [x for x in string.ascii_uppercase]
changed = True
letter = 'A'
old_letter = None
tmp = 0

while changed:
    for line in puzzle:
        if letter == old_letter:
            tmp += 1
        else:
            letter = old_letter
            tmp = 0
        old_list = new_list
        for i in range(26):
            if new_list[i] == line[5]:
                for j in range(26):
                    if new_list[j] == line[36]:
                        new_list.insert(i+tmp, new_list.pop(j))
    if old_list == new_list:
        changed = False


print ("".join(new_list))

"""

has = set()

working_on = [None] * 5
time_left = np.zeros(5, dtype=int)

for i in range(100000):
    for j in range(5):
        if working_on[j] is not None:
            time_left[j] -= 1
            if time_left[j] == 0:
                has.add(working_on[j])
                working_on[j] = None

    if set(s) == has:
        print()
        print(i)
        break

    for j in range(5):
        if working_on[j] is not None:
            continue

        for k in s:
            if k not in has and k not in working_on and req_dict[k] & has == req_dict[k]:
                working_on[j] = k
                time_left[j] = 60 + ord(k) - ord('A') + 1
                break
        #print (time_left)
