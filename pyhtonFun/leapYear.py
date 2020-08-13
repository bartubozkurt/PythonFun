# Python program to check if year is a leap year or not

'''
2017 is a not leap year
1900 is a not leap year
2012 is a leap year
2000 is a leap year
'''
# To get year from the user
year = int(input("Enter a year: "))

if (year % 4) == 0:
	if(year % 100) == 0:
		if (year % 400) == 0:
			print("{0} is a leap year".format(year))
		else:
			print:("{0} is not leap year".format(year))
	else:
		print("{0} is a leap year".format(year))
else:
	print("{0} is not a leap year".format(year))
