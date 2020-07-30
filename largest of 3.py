a,b,c=input("enter three numbers: ").split()
if (a>=b) and (a>=c):
    max=a
elif (b>=a) and (b>=c):
    max=b
else:
    max=c
print("largest of {0},{1} and {2} is".format(a,b,c),max)