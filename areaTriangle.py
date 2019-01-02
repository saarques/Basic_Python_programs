a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))
c = float(input("Enter length of side c: "))

# We are using Heron's formula here to calculate the area
s= (a+ b+ c)/2

area = (s*(s-a)*(s-b)*(s-c))**0.5

print("The area of the Triangle is: %0.2f"%(area))