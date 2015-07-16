''' Find the first number > 40755 that is Triangle, Pentagonal and Hexagonal
Tn = n(n+1)/2
Pn = n(3n-1)/2
Hn = n(2n-1)'''

def Tgen():
	n = 1
	while True:
		yield (n*(n+1))/2
		n += 1

def Pgen():
	n = 1
	while True:
		yield (n*(3*n-1))/2
		n += 1

def Hgen():
	n = 1
	while True:
		yield n*(2*n-1)
		n += 1

def check(num, T, P, t, p):
	while True:
		while t < num:
			t = T.next()
		if t > num:
			return t, p
		while p < num:
			p = P.next()
		if p > num:
			return t, p
		print num, t, p
		return t, p

T, P = Tgen(), Pgen()
t, p = T.next(), P.next()
#n = 0
for h in Hgen():
	t, p = check(h, T, P, t, p)
#	n += 1
#	if  n % 10**5 == 0:
#		print n, h
