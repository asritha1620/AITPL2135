n=int(input("enter number of rows: "))
for i in range(1,n+1):
    k=1
    for j in range(1,n-i+1):
        print(end="  ")
    for j in range(i,0,-1):
        print(k,end=" ")
        if k==1:
           k=0
        else:
           k=1
    for j in range(2,i+1):
        print(k,end=" ")
        if k==1:
            k=0
        else:
            k=1
    print()

