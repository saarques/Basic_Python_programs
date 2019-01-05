n= int(input("Enter the first number: "))
m= int(input("Enter the second number: "))
l= int(input("Enter the third number: "))

a= int(input("Enter the number upto which you want the series: "))

def sequenceThree(c):
	if c==0:
		return n
	elif c==1:
		return m
	elif c==2:
		return l
	elif c==3:
		return l+ m+ n
	else:
		return 2*sequenceThree(c-1)- sequenceThree(c-4)

# print("The value at number 7 in the sequence is: {}".format(sequenceThree(7-1)))

for i in range(a):
	print(sequenceThree(i), end = ', ')
print(". . . . .")
