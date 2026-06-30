a=int(input("enter number:"))
if a>-10 and a<10:
	print("number is single digit")
elif a>-100 and a<100:
	print("number is double digit")
elif a>-1000 and a<1000:
	print("number is three digit")
else:
	print("more than three digit number")
	