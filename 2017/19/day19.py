f = open("./puzzle.txt").read()
grid = [line for line in f.split("\n")]

print(grid[0].index('|'))

#while True:

