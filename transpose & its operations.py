#transpose of a matrix
import numpy as n
a=[int(i) for i in input("enter 4 elements:").split()]
b=n.array([i for i in a]).reshape((2,2))
print(b)
print("Transpose of given matrix is:\n", b.transpose())


#arthimetic operations of a matrix with its transpose
import numpy as n
a=[int(i) for i in input("enter 8 elements:").split()]
c=n.array([i for i in a]).reshape((4,2))
b=c.transpose()
print(b)
d=print("product of the given matrix and its transpose is:\n",c.dot(b))





















































































