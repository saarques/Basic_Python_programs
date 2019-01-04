def add(x, y):
	return x+y

def sub(x, y):
	return x-y

def mul(x, y):
	return x*y

def div(x, y):
	return x/y

print("What do you want to do?\n")
print("1. Add")
print("2. Substract")
print("3. Multiply")
print("4. Division")

choice = int(input("Enter your choice(1/2/3/4): "))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice==1:
    print(add(num1, num2))
elif choice==2:
    print(sub(num1, num2)) 
elif choice==3:
	print(mul(num1, num2))
elif choice==4:
	print(div(num1, num2))
else:
	print("Invalid Choice!")