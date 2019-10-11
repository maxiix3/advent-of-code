from collections import defaultdict
timesheet = sorted(open('input.txt','r').read().splitlines())
guards = defaultdict(lambda:[0 for x in range(60)])

for event in timesheet:
    time, action = event.split('] ')
    time = time[12:]

    if 'Guard' in action:
        guard = int(action.split()[1][1:])
    elif action == 'falls asleep':
#        start = int(time.split(':')[0] + time.split(':')[1])  # fuck hours
        start = int(time.split(':')[1])
    elif action == 'wakes up':
#        stop = int(time.split(':')[0] + time.split(':')[1])   # fuck hours
        stop = int(time.split(':')[1])
        for x in range(start, stop):
            guards[guard][x] += 1

part1 = sorted(guards.keys(), key=lambda guard: -sum(guards[guard]))[0]
minute = guards[part1].index(max(guards[part1]))
print(int(part1)*minute)

part2 = sorted(guards.keys(), key=lambda guard: -max(guards[guard]))[0]
minute = guards[part2].index(max(guards[part2]))
print(int(part2)*minute)
