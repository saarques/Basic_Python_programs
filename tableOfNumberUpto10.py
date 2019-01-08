n = int(input("Enter the number you want the table of: "))

m = int(input("Enter the number upto which you want the table to be printed: "))

print("*"*40)
for i in range(m+1):
	print("{} x {} = {}".format(n, i, n*i))
print("*"*40)