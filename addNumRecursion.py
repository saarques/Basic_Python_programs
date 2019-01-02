n = int(input('Enter the number over which you want the sum of natural numbers: '))
def addNum(n):
	if n<1:
		return n
	else:
		return n+addNum(n-1)

sum = addNum(n)

print("The sum is: %d"%(sum))