def get_pivot(low, high):
	mid = (low+high)//2
	return mid

def quick_sort(a, low, high):
	pivotIndex = get_pivot(low, high)
	pivotValue = a[pivotIndex]
	border = low
	for index in range(low, high-1):
		if(a[index+1]<=pivotValue and a[border]>a[index+1]):
			a[border], a[index+1] = a[index+1], a[border]
			border += 1
	if a[border] >= a[pivotIndex]:
		a[border], a[pivotIndex] = a[pivotIndex], a[border]
	print(a)
	if low < pivotIndex:
		print(low, pivotIndex, "low")
		quick_sort(a, low, pivotIndex)
	if high > pivotIndex + 1:
		print(high, pivotIndex, "high")
		quick_sort(a, pivotIndex, high)

a = []
n = int(input("Size of array which is needed to be sorted: "))
for index in range(n):
	a.append(int(input()))
quick_sort(a, 0, len(a))
print(a)