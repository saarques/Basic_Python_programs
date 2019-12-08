def palindrome(s):
	count = 0
	for i in range(len(s)):
		if s[i] != s[-i-1]:
			if i==0:
				s = s[:]+s[i]
			else:
				s = s[:-i] + s[i] + s[-i:]
			count += 1
	print("Palindrome string: ", s, "\n No. of elements required to make it a palindrome: ", count)

s = str(input("Enter a string: "))
palindrome(s)