a=int(input("Enter position of Cat A: "))
b=int(input("Enter position of Cat B: "))
c=int(input("Enter position of Mouse: "))
if abs(a-c)>abs(b-c):
	print("Cat B")
elif abs(a-c)<abs(b-c):
	print("Cat A")
else:
	print("Mouse runs as cats fight, Bingo :)")