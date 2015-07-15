''' Problem 44
Pentagon numbers are: Pn = n(3n-1)/2
so it's: 1, 5, 12, 22, 35, 51, 70, 92, 117, 145
For some x in Pn, their sum and their difference are in Pn themselves.
Find the Pentagon numbers with the smallest difference who fullfill this criterion.
What's their difference?'''


def pents():
	n = 0
	while True:
		n += 1
		yield (n*(3*n-1))/2

def compare(curPn, Pnset):
	diff = curPn
	for val in Pnset:
		if curPn + val in Pnset:
			if curPn-val in Pnset:
				print val, curPn
				if diff > curPn-val:
					diff = curPn - val
					print diff
	if diff == curPn:
		return 0
	return diff

Pgen1, Pgen2 = pents(), pents()
Pnset, diff = set([Pgen2.next()]), 0


for curPn in Pgen1:
	while 2*curPn > max(Pnset):
		Pnset.add(Pgen2.next())
	curdiff = compare(curPn, Pnset)
	if curdiff:
		if diff == 0 or curdiff < diff:
			diff = int(curdiff)
			print diff
	if curPn % 1000 == 0:
		Pnlist = list(Pnset)
		Pnlist.sort()
		print Pnlist[-1]
		print curPn - Pnlist[Pnlist.index(curPn)-1], diff
		if curPn - Pnlist[Pnlist.index(curPn)-1] > diff and diff > 0:
			print "This is the answer: %s" % diff
			exit()



