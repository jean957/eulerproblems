# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

summe = 0
current = 1

def check(current):
	number = 0
	original = int(current)
	while current > 0:
		number += (current % 10)**5
		current /= 10
	if number == original:
		return number
	else:
		return 0

while True:
	current += 1
	if check(current) != 0:
		summe += check(current)
		print current, summe


