''' count the number of words in p042_words.txt, for which the sum of their letter-values is a triangle number'''

wfile = open('./p042_words.txt')

words = wfile.read().replace('"', '').lower()

wordlist, offset, count, triangles= words.split(','), ord('a')-1, 0, [1, 3, 6]

def triang(triangles):
	triangles.append(1+2*triangles[-1]-triangles[-2])

for i in range(5):
	triang(triangles)

for word in wordlist:
	curnum = 0
	for char in word:
		curnum += ord(char) - offset
	while curnum > triangles[-1]:
		triang(triangles)
	if curnum in triangles:
		count += 1
		if count % 50 == 0:
			print count, word

print count, triangles[-1]