from collections import defaultdict
lines = open("./puzzle.txt").readlines()

prog = []
reg0 = defaultdict(int)
reg1 = defaultdict(int)
reg1['p'] = 1
regs = [reg0,reg1]

for line in lines:
    line = line.strip().split()
    prog.append(line)

def get(value):
    try:
        return int(value)
    except ValueError:
        return reg[value]

tot = 0
ind = [0,0]
snd = [[],[]]
state = ['ok','ok']
pr = 0
reg = regs[pr]
i = ind[0]

while True:
    if prog[i][0] == 'snd':
        if pr ==1:
            tot +=1
        snd[pr].append(get(prog[i][1]))
    elif prog[i][0] == 'set':
        reg[prog[i][1]] = get(prog[i][2])
    elif prog[i][0] == 'add':
        reg[prog[i][1]] += get(prog[i][2])
    elif prog[i][0] == 'mul':
        reg[prog[i][1]] *= get(prog[i][2])
    elif prog[i][0] == 'mod':
        reg[prog[i][1]] %= get(prog[i][2])
    elif prog[i][0] == 'rcv':
        if snd[1-pr]:
            state[pr] = 'ok'
            reg[prog[i][1]] = snd[1-pr].pop(0)
        else:
            if state[1-pr] == 'done':
                break #deadlock
            if len(snd[pr])==0 and state[1-pr] == 'r':
                break # stuck
            ind[pr] = i
            state[pr] = 'r'
            pr = 1 - pr
            i = ind[pr]-1
            reg = regs[pr]
    elif prog[i][0] == 'jgz':
        if get(prog[i][1]) > 0:
            i += get(prog[i][2])-1
    i += 1
    if not 0<=i<len(prog):
        if state[1-pr] == "done":
            break
        state[pr] = "done"
        ind[pr] = i
        pr = 1 - pr
        i = ind[pr]
        reg = regs[pr]

print tot
