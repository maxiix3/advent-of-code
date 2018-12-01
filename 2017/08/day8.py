dic = {}
f = open("./puzzle.txt", 'r').readlines()
maximum = 0
for line in f:
    L = line.split()
    if L[0] not in dic:
        dic[L[0]] = 0
    if L[-3] not in dic:
        dic[L[-3]] = 0
    if L[-2] == "<":
        if dic[L[-3]] <  int(L[-1]):
            if L[1] == 'inc':
                dic[L[0]] += int(L[2])
            else:
                dic[L[0]] -= int(L[2])
    if L[-2] == "<=":
        if dic[L[-3]] <= int(L[-1]):
            if L[1] == 'inc':
                dic[L[0]] += int(L[2])
            else:
                dic[L[0]] -= int(L[2])
    if L[-2] == ">":
        if dic[L[-3]] >  int(L[-1]):
            if L[1] == 'inc':
                dic[L[0]] += int(L[2])
            else:
                dic[L[0]] -= int(L[2])
    if L[-2] == ">=":
        if dic[L[-3]] >= int(L[-1]):
            if L[1] == 'inc':
                dic[L[0]] += int(L[2])
            else:
                dic[L[0]] -= int(L[2])
    if L[-2] == "==":
        if dic[L[-3]] == int(L[-1]):
            if L[1] == 'inc':
                dic[L[0]] += int(L[2])
            else:
                dic[L[0]] -= int(L[2])
    if L[-2] == "!=":
        if dic[L[-3]] != int(L[-1]):
            if L[1] == 'inc':
                dic[L[0]] += int(L[2])
            else:
                dic[L[0]] -= int(L[2])
    if dic[max(dic, key=dic.get)] > maximum:
        maximum = dic[max(dic, key=dic.get)]
print(dic[max(dic, key=dic.get)])
print("maximum", maximum)
