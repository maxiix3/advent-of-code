# first task
import numpy as np
grid = np.zeros((1000,1000))
data = open("six.txt")
lines = data.readlines()
lights = 0
for line in lines:
    instruks, fra, tmp, til = line.strip().rsplit(' ', 3)
    fra = [int(kordinat) for kordinat in fra.split(',')]
    til = [int(kordinat) for kordinat in til.split(',')]
    for i in range(fra[0], til[0] + 1):
        for j in range(fra[1], til[1] + 1):
            if instruks == 'turn on' :
                if grid[i][j] == 0:
                    lights += 1
                grid[i][j] = 1
            elif instruks == 'turn off' :
                if grid[i][j] != 0:
                    lights -= 1
                grid[i][j] = 0
            elif instruks == 'toggle' :
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    lights -= 1
                else:
                    grid[i][j] = 1
                    lights += 1
print lights

# extra
lights = 0
grid = np.zeros((1000,1000))
for line in lines:
    instruks, fra, tmp, til = line.strip().rsplit(' ', 3)
    fra = [int(kordinat) for kordinat in fra.split(',')]
    til = [int(kordinat) for kordinat in til.split(',')]
    for i in range(fra[0], til[0] + 1):
        for j in range(fra[1], til[1] + 1):
            if instruks == 'turn on' :
                grid[i][j] += 1
                lights += 1
            elif instruks == 'turn off' :
                if grid[i][j] != 0:
                    lights -= 1
                    grid[i][j] -= 1
            elif instruks == 'toggle' :
               lights += 2
               grid[i][j] += 2
print lights
