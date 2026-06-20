num=int(input("enter number:"))
if num>=1 and num<=30:
	if num%6==1:
		print("group_1")
	elif num%6==2:
		print("group_2")
	elif num%6==3:
		print("group_3")
	elif num%6==4:
		print("group_4")
	elif num%6==5:
		print("group_5")
	elif num%6==6:
		print("group_6")
	else:
		print("no group found")
else:
	print("invalid number")