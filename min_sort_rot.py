# Considering the array to be distinct and rotated at some index
def find_minimum(a, n):
	for index in range(n-1):
		if a[index]>a[index + 1]:
			return a[index + 1]
		if a[index] < a[-1]:
			return a[index]

n = int(input("Enter size of array: "))
a = []
for index in range(n):
	a.append(int(input()))
print("**", find_minimum(a, n), "**")