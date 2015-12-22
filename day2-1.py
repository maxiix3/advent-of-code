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
