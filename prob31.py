# How many ways are there to make 2pounds

# You have 1p, 2p, 5p, 10p, 20p, 50p, 100p, 200p

# a + 2b + 5c + 10d + 20e + 50f + 100g + 200h = 200

count = 1

for aa in range(201):
	amount = aa
	for bb in range(101):
		amount = aa + bb*2
		if amount > 200:
			break
		for cc in range(41):
			amount = aa + bb*2 + cc*5
			if amount > 200:
				break
			for dd in range(21):
				amount = aa + bb*2 + cc*5 + dd*10
				if amount > 200:
					break
				for ee in range(11):
					amount = aa + bb*2 + cc*5 + dd*10 + ee*20
					if amount > 200:
						break
					for ff in range(5):
						amount = aa + bb*2 + cc*5 + dd*10 + ee*20 + ff*50
						if amount > 200:
							break
						for gg in range(3):
							amount = aa + bb*2 + cc*5 + dd*10 + ee*20 + ff*50 + gg*100
#							print amount, count, aa, bb, cc, dd, ee, ff, gg
#							if aa == 2:
#								exit()
							if amount > 200:
								break
							if amount == 200:
								count += 1
								print count, aa, bb



