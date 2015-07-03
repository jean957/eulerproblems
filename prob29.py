# How many distinct terms are in the sequence generated a**b for 0 < a and b < 100

terms = []

for ab in range(2, 101):
	for bc in range(2, 101):
		terms.append(ab**bc)

distinctterms = list(set(terms))

print len(distinctterms)
