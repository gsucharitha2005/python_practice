l=['']*5
print(l)
for x in range(5):
	l[x]=x
print(l)


def m1(a):
	print(a)
def m2(a):
	m1(a)
	print(a)
m2(10)

