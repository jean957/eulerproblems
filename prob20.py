# what is the sum of all digits in 100!

def faculty(num):
	if num == 0:
		return 1
	else:
		return num * faculty(num - 1)

number = faculty(100)
digit = 1
summe = 0

print number

while number != 0:
	digit = number % 10
	summe += digit
	number /= 10

print summe
