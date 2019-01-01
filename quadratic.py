# Program to find roots of a equation provided by the user

print("A quadratic equation is of the format : ax2+bx+c")
a= float(input("Enter value of a: "))
b= float(input("Enter value of b: "))
c= float(input("Enter value of c: "))
# Shri Dharacharya formula to calculate roots is: (-b+-sqrt(D))/2a, where D = b2-4ac

# roots be x1 and x2

D = b**2 - 4*a*c
if D>=0:
	rtD= D**0.5
	x1= (-b+rtD)/(2*a)
	x2= (-b-rtD)/(2*a)
	print("Roots for the provided equation are %f and %f "%(x1, x2))

else:
	print("No real roots exist! :(")

