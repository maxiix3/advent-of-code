import string as s
puzzle = open('input5.txt').read()
#puzzle = "dabAcCaCBAcCcaDA"

old = 2

while old != puzzle:
    old = puzzle
    for i in range(0,26):
        puzzle = puzzle.replace(chr(ord("a") + i) + chr(ord("A") + i),"")
        puzzle = puzzle.replace(chr(ord("A") + i) + chr(ord("a") + i),"")

print("Part1:", len(puzzle))

original = puzzle
shortest = 5000000
for i in range(26):
    puzzle = original
    puzzle = puzzle.replace(s.ascii_lowercase[i],'')
    puzzle = puzzle.replace(s.ascii_uppercase[i],'')
    while old != puzzle:
        old = puzzle
        for i in range(0,26):
            puzzle = puzzle.replace(chr(ord("a") + i) + chr(ord("A") + i),"")
            puzzle = puzzle.replace(chr(ord("A") + i) + chr(ord("a") + i),"")
        if len(puzzle) < shortest:
            shortest = len(puzzle)

print ("part 2:", shortest)

