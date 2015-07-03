print '''This is designed to calculate the Sum of all multiples of 3 or 5 < 1000 '''

aa = 3
ab = 5
ac = 15
ad = 0
multa = []
multb = []

while aa < 1000:
    multa.append(aa)
    aa = aa + 3

while ac < 1000:
    multa.remove(ac)
    ac += 15


#print multa[]
#for bb in multa:
#    print bb

while ab < 1000:
    multb.append(ab)
    ab += 5

#print multb[]
#for bb in multb:
#    print bb

print '\n'

print multa
print multb

zz = multa[-1]
xx = 0

while xx != zz:
    xx = multa.pop(0)
    print xx
    ad = ad + xx

zzb = multb[-1]
xxb = 0

while xxb != zzb:
    xxb = multb.pop(0)
    print xxb
    ad = ad + xxb

print ad



