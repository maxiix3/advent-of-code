import hashlib as h
status = True
counter = 0
while status:
    string = "ckczppom" + str(counter)
    m = h.md5()
    m.update(string)
    resultat = m.hexdigest()
    if resultat.startswith('00000'):
        print "00000... = %d" %counter
    if resultat.startswith('000000'):
        print "000000... = %d" %counter
        break
    counter += 1
