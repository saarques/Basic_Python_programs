# Program t check if a number is divisible by another number or not.
a = int(input("Enter the number which is to be divided: "))

b = int(input("Enter the number which will be used to divide: "))

divide = lambda x, y: x%y==0

print("Status of divisibilty of {} by {} is: ".format(a, b), divide(a, b))