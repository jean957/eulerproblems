# find the shortest path

numbers = '''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

oldlist = numbers.split()

newlist = []

for aa in oldlist:
	newlist.append(int(aa))


def listnames(counter):
	name = 'line%d' % counter
	return name

counter = 0
current = 0
linelist = []
column = 0
line = 0

for i, val in enumerate(newlist):
	if i == counter + current:
		current += counter
		counter += 1
		line = listnames(counter)
		line = []
		linelist.append(line)
	line.append(val)

maxval = 0

def step(line, column, linelist, cur):
	global counter
	global maxval
	print cur, counter, line
	cur += linelist[line][column]
	if cur >= maxval:
		maxval = cur
	if line + 1 == counter:
		return cur
	else:
		return step(line+1, column, linelist, cur), step(line+1, column+1, linelist, cur)

step(0, 0, linelist, 0)

print maxval

