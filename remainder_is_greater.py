num=int(input("enter number:"))
a=num%4
b=num%5
if a>b:
	print(a)
elif b>a:
	print(b)
elif b==a:
	print("both are equal ")
else:
	print("invalid number")

	