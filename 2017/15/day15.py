input_a =  591
input_b = 393
fact_a = 16807
fact_b = 48271

a = [input_a*fact_a]
b = [input_b*fact_b]
a2 = []
b2 = []

div = 2147483647
counter = 0
counter2 = 0

for i in range(40000000):
    a.append((a[i]*fact_a)%div)
    b.append((b[i]*fact_b)%div)
    if a[i]%4 == 0:
        a2.append(a[i])
    if b[i]%8 == 0:
        b2.append(b[i])
    if (a[i] & 0xFFFF) == (b[i] & 0xFFFF):
        counter += 1

for i in range(5000000):
    if (a2[i] & 0xFFFF) == (b2[i] & 0xFFFF):
        counter2 += 1


print("day15_1:", counter)
print("day15_2:", counter2)

