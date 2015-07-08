'''Find the sum of all 0 - 9 pandigital numbers for which num(d2,d3,d4) % 2 == 0 
num(d3,d4,d5) % 3 == 0 and so on up to num(d8,d9,d10) % 17 == 0'''

divs = [2,3,5,7,11,13,17]


def check(divs, numb):
	for d in range(7):
		if int(str(numb[d+1])+str(numb[d+2])+str(numb[d+3])) % divs[d] != 0:
			return False
	return True


def assemble(numb):
	mystr = '%d%d%d%d%d%d%d%d%d%d' % (numb[0],numb[1],numb[2],numb[3],numb[4],numb[5],numb[6],numb[7],numb[8],numb[9])
	return int(mystr)

def generate():
	numb = [9]
	for a in range(2):
		numb.insert(a, 8)
		for b in range(3):
			numb.insert(b, 7)
			for c in range(4):
				numb.insert(c, 6)
				for d in range(5):
					numb.insert(d, 5)
					for e in range(6):
						numb.insert(e, 4)
						for f in range(7):
							numb.insert(f, 3)
							for g in range(8):
								numb.insert(g, 2)
								for h in range(9):
									numb.insert(h, 1)
									for i in range(9):
										numb.insert(i+1, 0)
										yield numb
										numb.remove(0)
									numb.remove(1)
								numb.remove(2)
							numb.remove(3)
						numb.remove(4)
					numb.remove(5)
				numb.remove(6)
			numb.remove(7)
		numb.remove(8)

sum = 0

for numb in generate():
	if check(divs, numb):
		sum += assemble(numb)
		print numb, sum



