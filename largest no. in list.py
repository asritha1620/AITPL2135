l=[]
n=int(input("enter number of elements in the list: "))
for i in range(n):
    l.append(int(input("enter element: ")))
l.sort()
print("largest number in the given list is:",l[-1])