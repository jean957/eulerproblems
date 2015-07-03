# sort the names in p022_names.txt than sum the multiplications of the sum of their letters with their place in the ordered list

summe = 0

namefile = open('./p022_names.txt')

names = namefile.read().replace('"', '').lower()

namelist = names.split(',')

namelist.sort()

def numberize(letter):
	return ord(letter) - 96

for i, val in enumerate(namelist):
	zwischen = 0
	for char in val:
		zwischen += numberize(char)
	summe += (i+1) * zwischen
	print i, val, zwischen

print summe
