n = input()
sum = 0
i= 0
while i < len(n):
	sum = sum + int(n[i])**3
	i = i + 1
else:
    if int(n) == sum:
    	print("Armstrong Number!")
    else:
        print("Not a Armstrong Number!") 