# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

summe = 0
end = 0

def faculty(num):
	if num == 0:
		return 1
	if num == 1:
		return 1
	else:
		return faculty(num -1) * num

def check(current):
	number = 0
	digit = 0
	original = int(current)
	while current > 0:
		digit = current % 10
		number += faculty(current % 10)
		current /= 10
	if number == original:
		print number
		return number
	else:
		return 0

for val in range(20):
	if end > faculty(9) * val:
		end = faculty(9) * val
		break
	end += 9 * 10**val

for current in range(10, end+1):
	summe += check(current)
	if current % 100000 == 0:
		print current, summe
