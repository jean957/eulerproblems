# counting Sundays

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

year = 1900
day = 0
sundays = 0

def funyear(year, day, sundays):
	day, sundays = lmonth(day, sundays)
	day, sundays = febmonth(day, sundays)
	if year % 4 == 0:
		day = (day + 1) % 7
	day, sundays = lmonth(day, sundays)
	day, sundays = smonth(day, sundays)
	day, sundays = lmonth(day, sundays)
	day, sundays = smonth(day, sundays)
	day, sundays = lmonth(day, sundays)
	day, sundays = lmonth(day, sundays)
	day, sundays = smonth(day, sundays)
	day, sundays = lmonth(day, sundays)
	day, sundays = smonth(day, sundays)
	day, sundays = lmonth(day, sundays)
	return year + 1, day, sundays

def lmonth(day, sundays):
	if day == 6:
		sundays += 1
	return (day + 31) % 7, sundays

def smonth(day, sundays):
	if day == 6:
		sundays += 1
	return (day + 30) % 7, sundays

def febmonth(day, sundays):
	if day == 6:
		sundays += 1
	return (day + 30) % 7, sundays


while year < 2001:
	year, day, sundays = funyear(year, day, sundays)

year, day, sun19 = funyear(1900, 0, 0)

print year, day, sundays - sun19
