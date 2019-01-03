n = int(input("Enter the year: "))

if n%4 == 0:
	if n%100 == 0:
		if n%400 == 0:
			print("%d is a leap year!"%(n))
		else:
			print("{} is not a leap year!".format(n))
	else:
		print("%d is a leap year!"%(n))
else:
	print("{} is not a leap year!".format(n))