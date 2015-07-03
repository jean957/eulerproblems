# the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers. 

# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.

from math import sqrt

summe = 0

listabundant = []
abundantsums = []

def divissum(number):
	summe = 0
	for ab in range(1, 1 + int(sqrt(number))):
		if number % ab == 0:
			summe += ab + number / ab
	if sqrt(number) == int(sqrt(number)):
		summe -= int(sqrt(number))
	return summe - number

for ab in range(28123):
	if divissum(ab) > ab:
		listabundant.append(ab)

length = len(listabundant)

for ab in range(length):
	for val in listabundant:
		abundantsums.append(val + listabundant[0])
		print listabundant[0], val
	listabundant.pop(0)

abundantsums = list(set(abundantsums))

relevantabundant = [ab for ab in abundantsums if ab < 28124]		

for ab in range(28124):
	summe += ab

for ab in relevantabundant:
	summe -= ab

print summe

