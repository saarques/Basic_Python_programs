n = int(input("Enter the first number: "))
m = int(input("Enter the second number: "))

def gcd(n, m):
	if n>=m:
		for index in range(m+1, 0, -1):
			if n%index==0 and m%index==0:
				print("GCD is %d"%(index))
				break
	else:
		for index in range(n+1, 0, -1):
			if n%index==0 and m%index==0:
				print("GCD is %d"%(index))
				break
gcd(n, m)