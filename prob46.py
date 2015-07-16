'''Goldbachs other conjecture

which is the smallest odd composite number that can be written
as the sum of a prime and twice a square?
(e.g.: 15 = 7 + 2*2^2)
'''

from math import sqrt

primes, squares = [2, 3, 5, 7, 11, 13, 17, 19, 23], [2, 8]

def appendprimes(primes):
	# appends 20 primes to the given list of primes
	# must get a complete list of primes starting with 2 as input
	current = primes[-1] + 2
	count = 0
	while count != 20:
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

def appendsquares(squares):
	cur = 1+sqrt(squares[-1]/2)
	for i in range(20):
		squares.append(2*((cur+i)**2))

def check(num, squares, primes):
	if num in primes[-25:]:
		return
	cursq, count = squares[-1], 0
	for prime in primes:
		while prime + cursq > num:
			count += 1
			if cursq == 2:
				print num, 'xXx'
				return
			cursq = squares[-count]
		if prime + cursq == num:
			return

n = 3
while True:
	n += 2
	if squares[-1] < n:
		appendsquares(squares)
	if primes[-1] < n:
		appendprimes(primes)
	if n % 10000 == 1:
		print n
	check(n, squares, primes)




