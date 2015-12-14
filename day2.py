# task
f = open('two.txt')
sumkvm = 0
lines = f.readlines()
for line in lines:
    verdi = line.split('x')
    l = int(verdi[0])
    w = int(verdi[1])
    h = int(verdi[2])
    foo = [l*w, w*h, h*l]
    small = int(min(foo))
    kvm = (2 * l * w) + (2 * w * h) + (2 * h * l) + small
    sumkvm += kvm
f.close

print "papir =  %d" %sumkvm


# extra
import copy as c
f = open('two.txt')
sumribbon = 0
lines = f.readlines()
for line in lines:
    verdi = line.strip().split('x')
    l = int(verdi[0])
    w = int(verdi[1])
    h = int(verdi[2])
    foo = [l*w, w*h, h*l]
    volum = l*w*h
    tmp = c.copy(verdi)
    tmp = map(int, tmp)
    big = max(tmp)
    tmp.remove(big)
    side1 = int(tmp[0])
    side2 = int(tmp[1])
    ribbon = side1+side1 + side2+side2 + volum
    sumribbon += ribbon

f.close
print "ribbon = %d" %sumribbon
