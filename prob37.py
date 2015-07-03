from math import sqrt

'''The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from 
left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.'''

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

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

def truncleft(primes, number):
	while number > 9:
		newnum = number % 10**(len(str(number))-1)
		if newnum not in primes:
			return False
		number = int(newnum)
	return True
	
def truncright(primes, number):
	while number > 9:
		number /= 10
		if number not in primes:
			return False
	return True

def findtrunc(primes, next):
	while True:
		curprime = primes[next]
		next += 1
		if next >= len(primes):
			primes = appendprimes(primes)
		if truncleft(primes, curprime) and truncright(primes, curprime):
			return curprime, next

summe, next = 0, 7
for i in range(11):
	answer = findtrunc(primes, next)
	print answer
	summe += answer[0]
	print summe
	next = answer[1]
print summe




