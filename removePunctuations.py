punctuations = '!@#$%^&*_[]'

cleaned_string = ''

string = str(input('Enter the string you want to clean(without punctuations): '))

for char in string:
	if char not in punctuations:
		cleaned_string += char

print("Cleaned String :", cleaned_string)