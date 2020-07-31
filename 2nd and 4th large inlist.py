l=[]
n=int(input("enter number of elements in the list: "))
if n<2:
    print("can't find required largest numbers")
for i in range(n):
    l.append(int(input("enter element:")))
l.sort()
if n >= 4:
    print("2nd largest is:",l[-2] ,"and 4th largest is :",l[-4])
else:
    print("2nd largest is", l[-2] ,"\n length less than 4")

