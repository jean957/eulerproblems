''' if you concatenate integers like: 0.1234567891011121314... and call the 11th digit (0) 'd11'
find d1 * d10 * ... * d1000000'''

count, lim, solu = 0, 1, 1

for i in range(1, 400000):
	count += len(str(i))
	if count >= lim:
		solu *= int(str(i)[-(1+count-lim)])
		lim *= 10
		print solu, i
		if lim == 10**7:
			break

print solu