n = str(input("Enter the string you want to check if it is a palindrome or not!: "))

d = len(n)

flag = 0
for x in range(d//2):
	if n[x]==n[d-x-1]:
		pass
	else:
		flag = 1
if not flag:
	print("Given string is a Palindrome ^_^")
else:
	print("Given string is not a Palindrome :(")
