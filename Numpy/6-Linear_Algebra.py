# Linear Algebra in Numpy:

import numpy as np
a=np.ones((2,3))
b=np.full((3,2),2)
print(a)
print(b)


# matrix multiplication:
print(np.matmul(a,b))



# determinant of identity matrix:
c=np.identity(2)
print(c)

print(np.linalg.det(c))



# Inverse of a Matrix (Multiplicative  Inverse):
d=np.array([[1,2],[3,4]])
print(d)

print(np.linalg.inv(d))


# Eigen Values of Square matrix:
e=np.ones((2,2))
print(e)

print(np.linalg.eig(e))



# Trace :
f=np.full((3,3),5)
print(f)

print(f.trace())