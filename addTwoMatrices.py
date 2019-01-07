# Program to add two matrices

n, m, c= [], [], []

l = int(input("Enter the size of the square matrix: "))

print("*"*40)

for index in range(l*l):
	n.append(eval(input("Enter the {}th value for matrix n: ".format(index))))

print("*"*40)

for index in range(l*l):
	m.append(eval(input("Enter the {}th value for matrix m: ".format(index))))

print("*"*40)

for i in range(l*l):
	c.append(n[i]+ m[i])

print("Solution matrix: ")

a=0
for i in range(l):
	b =(i + 1)*l
	print(c[a: b])
	a = b