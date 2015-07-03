from math import sqrt

# the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000

number = 1
amisum = 0

def divissum(number):
	summe = 0
	for ab in range(1, 1 + int(sqrt(number))):
		if number % ab == 0:
			summe += ab + number / ab
	if sqrt(number) == int(sqrt(number)):
		summe -= int(sqrt(number))
	return summe - number

while number < 9999:
	number += 1
	current = divissum(number)
	if current > number:
		if number == divissum(current):
			amisum += number + current

print amisum


		
