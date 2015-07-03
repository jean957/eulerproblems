# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

summe = 1
squaresize = 1
count = 1


while squaresize < 1000:
	squaresize += 2
	for ab in range(4):
		count += squaresize - 1
		summe += count
		print count

print summe, squaresize, count
	