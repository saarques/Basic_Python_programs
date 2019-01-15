# In this program we are going to take three numbers as input and print the greatest number among them

n = []

for index in range(3):
	n.append(eval(input("Enter the number: ".format(index))))

print(max(n))