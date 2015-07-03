# What is the first term in the Fibonacci sequence to contain 1000 digits

ab = 1
ac = 1
count = 2

while True:
	ab += ac
	ac += ab
	count += 2
	if ac > 10**999:
		if ab > 10**999:
			print count - 1
		else:
			print count
		break



