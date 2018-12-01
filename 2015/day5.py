# original
inputfile  = open("five.txt").read().split()
vowels = ['a','e','i','o','u']
lookup = ['ab','cd','pq','xy']
nice = 0
nice2 = 0
naughty = 0
for word in inputfile:
    counter = 0
    double = False
    for i in range(len(word)):
        if word[i] in vowels:
            counter += 1
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            double = True
        tmp = word[i] + word[i+1]
        if tmp in lookup:
            double = False
            counter = 0
            break
    if counter >= 3 and double == True:
        nice += 1

print nice

# extra
for word in inputfile:
    repeat = False
    status = False
    for i in range(len(word)-2):
        if word[i] == word[i+2]:
            repeat = True
        sub = word[i: i+2]
        if sub in word[i+2 :]:
            status = True

    if status and repeat:
        nice2 += 1


print nice2
