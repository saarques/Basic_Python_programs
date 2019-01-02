n = int(input("Enter the number: "))

for i in range(2, n):
	if n%i==0:
		print("Not a Prime Number!")
		break
	if i==n-1:
		print("Prime number!")