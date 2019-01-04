n = int(input("Enter the first number: "))
m = int(input("Enter the second number: "))

if n>m:
	greater=n
else:
	greater=m

def lcm():
	global greater
	lcm = 0
	while(True):
		if (greater%n==0) and (greater%m==0):
			lcm=greater
			break
		else:
			greater += 1
	return lcm

a = lcm()

print("The LCM for {} and {} is {}".format(n, m, a))