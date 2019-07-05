# Program to rotate a n-size array d no of times

# METHOD 1
def rotate(arr, n, d):
	for i in range(d):
		arr.append(arr[0])
		arr.remove(arr[0])
	return arr
# *****************************************

# GENERAL CODE
ar = []
n = int(input("Enter the size of the array: "))

for i in range(n):
	ar.append(input("Enter value at index {} : ".format(i)))

d = int(input("Enter the no of places you want to rotate the array: "))
# *****************************************
result1 = rotate(ar, n, d)
print("The output rotated array by METHOD 1 is : ", result1)

# METHOD 2
result2 = ar[d:] + ar[:d]
print("The output rotated array by METHOD 2 is : ", result2)