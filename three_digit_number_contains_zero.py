digit=int(input("enter digit:"))
if digit>99 and digit<=999:
	if str(0) in str(digit): 
		print("contain 0")
	else:
		print("0 is not contain")
else:
	print("invalid number")
