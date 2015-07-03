# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

from math import sqrt

primes = [2, 3]
currentmax = 0

def appendprimes(primes):
	current = primes[-1] + 2
	count = 0
	while count != 5:
		end = int(2 + current / 2)
		for div in range (2, end):
			if div == end - 1:
				primes.append(current)
				count += 1
				current += 2
			if current % div == 0:
				current += 2
				break
	return primes

def check(number, primes):
	for val in primes:
		if number % val == 0:
			if number == val:
				continue
			return False
	return True

for mult in range(-999, 1000):
	for add in range(-999, 1000):
		n = -1
		while True:
			n += 1
			number = n*n + mult*n + add
			if number < 0:
				break
			if sqrt(number) + 1 > primes[-1]:
				primes = appendprimes(primes)
			if check(number, primes):
				continue
			break
		if n > currentmax:
			currentmax = int(n)
			print currentmax, mult * add
		if n == currentmax:
			currentmax = int(n)
			print 'Equal:', currentmax, mult * add

print currentmax
		
