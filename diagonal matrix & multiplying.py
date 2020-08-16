#diagonal matrix and multiply it with 4*2 matrix
import numpy as n
a=n.diag([1,2,3,4])
print(a)
b=n.array([[3,6],[8,2],[9,1],[5,7]])
print(b)
print("product of diagonal matrix and the given 4x2 matrix is:\n",a.dot(b))
