# In this program, we are going to implement the reduce function.

from functools import reduce

n = []
l = int(input("Enter the number of elements in the list: "))
for index in range(l):
	n.append(eval(input("Enter the {} value: ".format(index+1))))

print("Product of the elements of the list: ", reduce(lambda x, y: x*y, n))