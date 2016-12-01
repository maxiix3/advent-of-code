import bitarray

f = open("day7.txt")
lines = f.readlines()
for line in lines:
    words = line.split()
    if 'NOT' in words:
        words[3] = words[1]
    elif 'OR' in words:
        words[4] = words[0] | words[2]
    elif 'LSHIFT' in words:
        words[4] = words[0] << words[2]
    elif 'RSHIFT' in words:
        words[4] = words[0] << words[2]
    elif 'AND' in words:
        words[4] = words[0] & words [2]
    else:
        words[3] = words[0]

        a = int('dq')

