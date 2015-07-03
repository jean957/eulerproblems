print 'This is a design to find the sum of all even-valued fibonacci-numbers < 4M'

aa = 1
ab = 2
tt = 2
xx = 0

even = []

while tt < 4000003:
    even.append(tt)
    tt += 2


while aa < 4000000 and ab < 4000000:
#    print aa, '\t', ab
    
    if aa in even:
        xx += aa
    else:
        pass
    
    if ab in even:
        xx += ab
    else:
        pass
    
#    print xx
    
    aa += ab
    ab += aa

print xx

