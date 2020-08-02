x=input("enter the elements to check:")
l=[int(i) for i in x.split()]
pos=list(filter(lambda n:n>0,l))
neg=list(filter(lambda n:n<0,l))
print("positive numbers are:",pos)
print("negative numbers are:",neg)
