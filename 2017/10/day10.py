from collections import deque
from functools import reduce

def day10(l, data, pos, skip_size):
    for num in data:
        l = deque(l)
        l.rotate(-pos)
        l = list(l)
        l[:num] = reversed(l[:num])
        l = deque(l)
        l.rotate(pos)
        l = list(l)
        pos += num + skip_size
        skip_size += 1
    return l, pos, skip_size


def knot_hash(data, l=256):
    data = [ord(i) for i in data]
    data = data[:] + [17, 31, 73, 47, 23]
    pos = 0
    skip_size = 0
    l = range(l)

    for i in range(64):
        l, pos, skip_size = day10(l, data, pos, skip_size)

    dense = [reduce(lambda x, y: x ^ y,l[i:i + 16])
             for i in range(0, len(l), 16)]

    hex_hash = ''
    for i in dense:
        hex_hash += "%02x" % i
    return hex_hash


if __name__ == "__main__":
    data = open("./puzzle.txt", "r").readline()
    f = eval('[' + data.rstrip() + ']')
    l = list(range(256))
    skip_size = 0
    pos = 0
    knot, _, _, = day10(l, f, pos, skip_size)
    print ("day10_1:", knot[0]*knot[1])
    data = data[:-1]
    print("day10_2", knot_hash(data, 256))
