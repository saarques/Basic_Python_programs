n = int(input("Enter the first number: "))
m = int(input("Enter the second number: "))
l = int(input("Enter the third number: "))

def isDivisible(x):
	# We'll pre-compute the 3rd term of the sequence
    l = [1,1,3]
    # We will compute the modulus of the sequence
    #     until we generate a 0,
    #     or we repeat to 1,1,1
    while (l[2] > 0 and l[0]*l[1]*l[2]!=1):
    	l = [l[1], l[2], sum(l) % x]
    #if we generated a 0, x is divisible
    if l[2]==0:
    	return x
    else:
    	return 0


a= []
while(True):
	for i in range(1, 1000, 2):
		if isDivisible(i)==i:
			a.append(i)
		if len(a)==10:
			print(a[9])
			break
	break

