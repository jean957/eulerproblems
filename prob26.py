
print 'Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.'


def next(divid, divis):
    divid *= 10
    divid %= divis
    return divid

highestcount = 0
highestdiv = 0


for divis in range(2, 1000):
    liste = []
    counter = 1
    divid = 1
#    print 'XXXXXXXX', divis, 1.0 / divis
    while divid not in liste:
        liste.append(divid)
        divid = next(divid, divis)
#    print liste, divid
    while divid != liste[-counter]:
        counter += 1
    if counter > highestcount:
        highestcount = counter
        highestdiv = divis

print highestdiv, highestcount

