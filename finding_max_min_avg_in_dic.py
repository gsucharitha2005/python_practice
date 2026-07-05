dic={"emp1":100,"emp2":200,"emp3":300,"emp4":400,"emp5":500,"emp6":600,"emp7":700,"emp8":800}

total=dic["emp1"]+dic["emp2"]+dic["emp3"]+dic["emp4"]+dic["emp5"]+dic["emp6"]+dic["emp7"]+dic["emp8"]
print("total:",total)
s=dic.values()
print(s)
len=len(s)
print("len:",len)
average=total/len
print("average:",average)
print("max:",max(s))
print("min:",min(s))
