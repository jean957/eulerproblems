''' Pandigital numbers make use of every digit 1 to n exactly once. What's the largest n pandigital prime?'''

from math import sqrt

def checkprime(potprime, primes):
	# is this number prime?
	end = int(sqrt(potprime))
	for prime in primes:
		if potprime % prime == 0:
			return False
		if prime >= end:
			return True

	for i in xrange(primes[-1], end+3, 2):
		if potprime % i == 0:
			return False

	return True


def appendprimes(primes):
	# appends 50 primes to the given list of primes
	# must get a complete list of primes starting with 2 as input
	current = primes[-1] + 2
	count = 0
	while count != 50:
		end = int(sqrt(current))
		prime = primes[0]
		next = 0
		while prime < end:
			prime = primes[next]
			next += 1
			if current % prime == 0:
				current += 2
				break
			if prime >= end:
				primes.append(current)
				current += 2
				count += 1
	return primes

def integ(liste):
	number = ''
	for i in liste:
		number += str(i)
	return int(number)

# order = 0, 9, 90, 108, 189, 198

def pandig():
	num = 7654321
	while True:
		if len(set(str(num))) == len(str(num)) and '0' not in str(num) and '9' not in str(num) and '8' not in str(num):
			yield num
		num -= 2
	

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

appendprimes(primes)

for num in pandig():
	if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
		print 'num357', num
		continue
	if checkprime(num, primes):
		print 'Yeay', num
		exit()
		break