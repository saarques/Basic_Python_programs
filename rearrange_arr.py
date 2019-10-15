n = int(input("Enter size of array: "))
a = set()
for i in range(n):
	a.add(int(input()))
b = []
for i in range(len(a)):
	if i not in a:
		b.append(-1)
	else:
		b.append(i)
del(a)
print(b)
del(b)