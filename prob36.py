# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# 585 = 1001001001

def numberize(number):
	# takes a number and returns a list of its digits
	mynum, liste = str(number), []
	for char in mynum:
		liste.append(int(char))
	return liste

def binarize(number):
	binary = ''
	bina = 1
	while bina <= number:
		bina *= 2
		if number % bina >= bina/2:
			binary = str('1'+binary)
		else:
			binary = str('0'+binary)
	binary = str('0'+binary)
	return int(binary)

def palicheck(liste):
	for i in range(len(liste)/2):
		if liste[i] != liste[-(i+1)]:
			return False
	return True

summe = 0

for i in range(1, 10**6):
	if palicheck(numberize(i)) and palicheck(numberize(binarize(i))):
		summe += i
		print i, binarize(i), summe

print summe






