with open("day8.txt") as f:
    a = [line.strip().count('\\') + line.strip().count('"') + 2 for line in f]
    print sum(a)

