'''Using a combination of black square tiles and oblong tiles chosen from: 
red tiles measuring two units, green tiles measuring three units, and blue tiles measuring four units, 
it is possible to tile a row measuring five units in length in exactly fifteen different ways.

How many ways can a row measuring fifty units in length be tiled?'''

def addtiles(length):
	if length < 50:
		return addtiles(length+1) + addtiles(length+2) + addtiles(length+3) + addtiles(length+4)
	if length == 50:
		return 1
	else:
		return 0

def faculty(num):
	if num < 2:
		return 1
	return num * faculty(num-1)

summe, count = 0, 0

for black in range(51):
	amount = black
	for red in range(26):
		amount = black + red*2
		if amount > 50:
			break
		for green in range(18):
			amount = black + red*2 + green*3
			if amount > 50:
				break
			for blue in range(14):
				amount = black + red*2 + green*3 + blue*4
				if amount > 50:
					break
				if amount == 50:
					count += 1
					summe += faculty(black+red+green+blue) / faculty(black) / faculty(red) / faculty(green) / faculty(blue)

print count, summe