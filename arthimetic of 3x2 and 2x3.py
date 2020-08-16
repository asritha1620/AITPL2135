#perform 2x3 matrix,3x2 matrix arthimetic opertaions
import numpy as n
a=[int(i) for i in input("enter 6 elements:").split()]
b=n.array([i for i in a]).reshape((2,3))
print("first matrix is:\n",b)
c=[int(i) for i in input("enter 6 elements:").split()]
d=n.array([i for i in c]).reshape((3,2))
print("second matrix is:\n",d)
print("As the matrix are of different sizes addition and subtraction is not possible")
print("product of given matrices is:\n",b.dot(d))