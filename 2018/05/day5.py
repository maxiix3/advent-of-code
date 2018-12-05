import string as s

def bruteforce_replacement(puzzle):
    new = len(puzzle)
    old = 100000000000000000
    while old != new:
        old = new
        for i in range(len(puzzle)-1):
            if puzzle[i] == puzzle[i].lower():
                if puzzle[i].upper() == puzzle[i+1]:
                    puzzle = puzzle[:i]+puzzle[i+1:]
                    puzzle = puzzle[:i]+puzzle[i+1:]
                    #puzzle = puzzle[:i+1]+puzzle[i+2:]
                    #puzzle = puzzle[:i]+puzzle[i+1:]
                    break
            elif puzzle[i] == puzzle[i].upper():
                if puzzle[i].lower() == puzzle[i+1]:
                    puzzle = puzzle[:i]+puzzle[i+1:]
                    puzzle = puzzle[:i]+puzzle[i+1:]
                    #puzzle = puzzle[:i+1]+puzzle[i+2:]
                    #puzzle = puzzle[:i]+puzzle[i+1:]
                    break
        new = len(puzzle)
    return (len(puzzle))


puzzle = open('input5.txt').read()
#puzzle = "dabAcCaCBAcCcaDA"

#print ("part 1:", puzzle)

original = puzzle
shortest = 5000000
for i in range(26):
    puzzle = original
    puzzle = puzzle.replace(s.ascii_lowercase[i],'')
    puzzle = puzzle.replace(s.ascii_uppercase[i],'')
    removed = bruteforce_replacement(puzzle)
    if removed < shortest:
        shortest = removed

print ("part 2:", shortest)
