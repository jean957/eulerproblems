print '''This is designed to calculate the Sum of all multiples of 3 or 5 < 1000 '''

xx = 0
aa = 3
ab = 5
ac = 15



while aa < 1000:
    xx += aa
    aa += 3


print xx

while ab < 1000:
    xx += ab
    ab += 5

print '\n', xx, '\n'

while ac < 1000:
    print xx, ac
    xx -= ac
    ac += 15

print xx
