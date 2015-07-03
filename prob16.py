# compute the sum of the digits in 2^1000

number = 2**1000
digit = 1
divis = 10
summe = 0

print number

while number != 0:
	digit = number % 10
	summe += digit
	number /= divis
#	print 'number', number, 'summe', summe, 'divis', divis, 'digit', digit

print summe
