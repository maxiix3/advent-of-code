import operator

blocks = [int(values) for values in open ("./day6_puzzle.txt").readline().split()]
bank = []
bank2 = []
counter = 1
counter2 = 0
while True:
    index, value = max(enumerate(blocks), key=operator.itemgetter(1))
    blocks[index] = 0
    while value > 0:
        index += 1
        if index >= len(blocks):
            index = 0
        blocks[index] += 1
        value -= 1
    if blocks in bank2:
        print("day6_2", counter-counter2)
        break
    if blocks in bank:
        if counter2 == 0:
            bank2.append(list(blocks))
            counter2 = counter
            print("day6_1", counter)
        counter +=1
    else:
        bank.append(list(blocks))
        counter += 1
