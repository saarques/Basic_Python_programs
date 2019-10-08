n = int(input("Enter size of array: "))
a = []
for index in range(n):
	a.append(int(input()))

c = int(input("Enter number of times you want to right rotate the array: "))
print(a[n-c :]+a[0 : n-c])