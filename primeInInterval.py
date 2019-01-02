n= int(input("Enter the number: "))

for i in range(2, n):
	for j in range(2, i):
		if i%j==0:
			break
		if j==i-1:
			print("%d is a prime number!"%(i))