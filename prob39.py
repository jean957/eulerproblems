'''If p is the perimeter of a right triangle with sides (a, b, c) there are three solutions for p=120
(20, 48, 52), (24, 45, 51), (30, 40, 50)
For which value of p<=1000, is the number of solutions maximised?'''

sidesquares = dict()
for i in range(1, 502):
	sidesquares[i] = i**2

def pairs(sidelen, sidesquares=sidesquares):
	count = 0
	for a in range(1, sidelen/2):
		for b in range(a+1, sidelen/2+1):
			c = sidelen - (a + b)
			if c > sidelen/2+1:
				continue
			if c <= b:
				break
			if sidesquares[a]+sidesquares[b] == sidesquares[c]:
				count += 1
	return count

print pairs(120)
# exit()

curmax = (0, 0)
for i in range(1, 1001):
	current = pairs(i)
	if current > curmax[1]:
		curmax = (i, current)
		print curmax