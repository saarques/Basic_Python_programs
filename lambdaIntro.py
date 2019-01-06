# Program to return square of a number using lambda function.

double = lambda x: x**2

a = int(input("Enter the number you want the square of: "))

print("The square of {} is {}".format(a, double(a)))