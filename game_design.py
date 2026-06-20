import random
count=0
for x in range(10):
	user=int(input("guess the number :"))
	num=random.randint(0,9)
	if user==num:
		print("you won  the match :")
		count+=1
	else:
		print("Computer won the match : ")
if count==3:
	print("finally you win the game:")
else:
	print("finally you loss the game .....")
		