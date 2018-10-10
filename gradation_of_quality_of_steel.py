#seems like there is a bug! try entering values 51,0.9 and 3000 and check it out.
hardness=int(input("Enter hardness of steel: "))
carbon_content=int(input("Enter carbon content of the steel: "))
tensile_strength=int(input("Enter tensile strength of the steel: "))
h,c,t=hardness,carbon_content,tensile_strength
if (h>50 and c<0.7 and t>5600):
	print("Grade: 10")
elif ((h>50 and c<0.7) or t>5600):
	print("Grade:9")
elif (h>50 or (c<0.7 and t>5600)):
	print("Grade:8")
elif ((h>50 and t>5600) or c<0.7):
	print("Grade:7")
elif (h>50 or c<0.7 or t>5600):
	print("Grade:6")
elif (h<50 and c>0.7 and t<5600):
	print("Grade:5")
