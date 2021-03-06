'''Take the number 192 and multiply it by each of 1, 2, and 3:
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?'''

def checkn(nlen):
	number, biggest = 0, 0
	while True:
		numstr = ''
		number += 1
		for i in range(1, nlen+1):
			numstr = str(numstr+str(i*number))
		if len(numstr) < 9:
			continue
		elif len(numstr) == 9:
			if '0'not in numstr and len(set(numstr)) == 9:
				if int(numstr) > biggest:
					biggest = int(numstr)
		elif len(numstr) > 9:
			print numstr
			return biggest

biggest = 0

for i in range(2, 6):
	print checkn(i)