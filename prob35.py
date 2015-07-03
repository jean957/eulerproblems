# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# How many circular primes are there below one million?

from math import sqrt

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
count = 2			# otherwise 2 and 5 wouldn't count because of checkcircle

def checkcircle(current):
	# quickcheck whether this might be a circular prime
	for digit in numberize(current):
		if digit % 2 == 0:
			return False
		if digit == 5:
			return False
	return True

def checkprime(potprime, primes):
	# is this number prime?
	end = int(sqrt(potprime))
	prime = primes[0]
	next = 0
	while prime < end:
		prime = primes[next]
		next += 1
		if potprime % prime == 0:
			return False
		if prime >= end:
			return True
	print 'Error in checkprime'
	exit()

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

def numberize(number):
	# takes a number and returns a list of its digits
	liste = []
	newlist = []
	while number != 0:
		digit = number % 10
		liste.append(digit)
		number /= 10
	for i in range(len(liste)):
		newlist.append(liste.pop(-1))
	return newlist

def reassemble(liste):
	# takes a list of digits and returns a number
	# the first digit in the list will be last in the number, the rest will be in order
	number = 0
	item = liste.pop(0)
	liste.append(item)
	for i in range(len(liste)):
		number += liste.pop() * (10**i)
	return number

# This produces at least all primes less than 1 million
while primes[-1] < 1000000:
	primes = appendprimes(primes)
	print len(primes), primes[-1]

# This checks which of the primes just produced is circular
for number in primes:
	if checkcircle(number):
		trying = int(number)
		if trying > 1000000:
			print 'finish early', count
			exit()
		for i in range(len(numberize(number))):
			trying = reassemble(numberize(trying))
			if trying == number:
				count += 1
				print number
				break
			if checkprime(trying, primes):
				continue
			break
			# This would be slower than checkprime:
			#if trying not in primes:
			#	break

print count




