with open("day8.txt") as f:
    a = [len(line.strip()) - len(eval(line)) for line in f]
    print sum(a)
