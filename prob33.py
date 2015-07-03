# Look for fractions like 49 / 98 = 4 / 8 where you can strike the same number in the numerator and denominator

# There are exactly four non-trivial examples of this type of fraction, 30 / 50 = 3 / 5 is a trivial example

# They must be less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

numer = 1
denom = 1

def checksame(num, den):
	aa = num % 10
	bb = num / 10
	if aa == 0 or bb == 0 or den/10 == 0 or den % 10 == 0:
		return 0
	if aa == den/10:
		return bb, den % 10
	if bb == den % 10:
		return aa, den / 10
	if aa == den % 10:
		return bb, den / 10
	if bb == den/10:
		return aa, den % 10
	return 0

for num in range(10, 100):
	for den in range(num + 1, 100):
		try:
			aa, bb = checksame(num, den)
		except:
			continue
		if (aa + 0.0) / bb == (num + 0.0) / den:
			print num, den, numer, denom
			numer *= num
			denom *= den

print numer, denom


