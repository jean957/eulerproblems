print '''The following iterative sequence is defined for the set of positive integers:

n > n/2 (n is even)
n > 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 > 40 > 20 > 10 > 5 > 16 > 8 > 4 > 2 > 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?'''

start = 1
maximum = 1
current = 1

while start < 1000000:
	new = start + 1
	start += 1
	count = 0
#	print 'xxx', new
	while new != 1:
		count += 1
		if new % 2 == 0:
			new /= 2
		else:
			new = new * 3 + 1

#		print new
	if count > maximum: 
		maximum = count
		current = start
		print 'newmax', current, maximum

print current, maximum
