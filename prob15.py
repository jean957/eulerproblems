# Trying it recursively.

columns = 3
lines = 3
gridsize = input('which size is your grid? >>') - 2  # add 2

def step(columns, lines):
	if columns == 0:
		return 1
	if lines == 0:
		return 1
	else:
		return step(columns - 1, lines) + step(columns, lines - 1)

# print step(columns, lines)

# recursively is too slow, trying other

# the number of possibilities to get to a certain node in the expanding grid is equal to the number in pascals triangle.
# so I multiply the (gridsize / 2)th line of pascals triangle with itself and add all entries.

pascal = [1, 1]

def other(pascal, gridsize):
	pascalnew = [1]
	for i, val in enumerate(pascal):
		if i + 1 == len(pascal):
			pass
		else:
			pascalnew.append(pascal[i] + pascal[i + 1])
	pascalnew.append(1)
	if gridsize == 0:
		return pascalnew
	else:
		return other(pascalnew, gridsize - 1)

pascalnew = other(pascal, gridsize)

possibilities = 0

for aa in pascalnew:
	possibilities += aa*aa

print possibilities
