l=[]
n=int(input("enter number of elements in the list: "))
if n<3:
    print("can't find required smallest numbers")
for i in range(n):
    l.append(int(input("enter element:")))
l.sort()
if n>=5:
    print("3rd smallest is l[2] \n5th smallest is l[4]")
else:
    print("3rd smallest is l[2] \nlength is less than 5")