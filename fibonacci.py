n = int(input("Enter the number upto which you want the Fibonacci series to be printed: "))

def fibo(n):
	if n<=1:
		return n
	else:
		return fibo(n-1)+fibo(n-2) 

if n<=0:
    print("Please enter a positive number!")
else:
    print("Fibonacci series: ")
    for i in range(n):
        print(fibo(i)) 