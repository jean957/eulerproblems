# find the sum of all products of equations that contain all numbers for 0 < number < 10


def numberization(equation):
	liste2 = []
	for number in equation:
		while number != 0:
			digit = number % 10
			if digit == 0:
				return False
			liste2.append(digit)
			number /= 10
	if len(list(set(liste2))) == len(liste2) == 9:
		print equation[0], '*', equation[1], '=', equation[2]
		return True
	return False

summe = 0
liste = []

# for 1digit * 4digit = 4digit

print '1digit'

for aa in range(1, 10):
	for bb in range(1234, 9876):
		equation = [aa, bb, aa*bb]
		if equation[-1] > 9876:
			break
		if equation[-1] not in liste and numberization(equation):
			liste.append(equation[-1])
			summe += equation[-1]

# for 2digit * 3digit = 4digit
print '2digit'

for aa in range(11, 20):
	for bb in range(123, 987):
		equation = [aa, bb, aa*bb]
		if equation[-1] > 9876:
			break
		if equation[-1] not in liste and numberization(equation):
			liste.append(equation[-1])
			summe += equation[-1]

print '20 - 40'

for aa in range(21, 40):
	for bb in range(123, 498):
		equation = [aa, bb, aa*bb]
		if equation[-1] > 9876:
			break
		if equation[-1] not in liste and numberization(equation):
			liste.append(equation[-1])
			summe += equation[-1]

print '40 - 60'

for aa in range(41, 60):
	for bb in range(123, 249):
		equation = [aa, bb, aa*bb]
		if equation[-1] > 9876:
			break
		if equation[-1] not in liste and numberization(equation):
			liste.append(equation[-1])
			summe += equation[-1]

print '60 - 100'

for aa in range(61, 98):
	for bb in range(123, 164):
		equation = [aa, bb, aa*bb]
		if equation[-1] > 9876:
			break
		if equation[-1] not in liste and numberization(equation):
			liste.append(equation[-1])
			summe += equation[-1]

print summe

