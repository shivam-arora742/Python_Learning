# Working with numpy:

# first-> pip install numpy &

# Import numpy library to program.
import numpy as np;

# Creation of Array:
# 1-D array:
a=np.array([1,2,3,4,5])
print(a);           #printing array values.

# 2-D array:
b=np.array([[1.0 ,2.0 , 3.33],
            [22, 32.33, 100.01]])
print(b);

# Get Dimension of Array:
print(a.ndim)
print(b.ndim)

# Shape of Array:
print(a.shape)   #for 1-D returns no of elements.
print(b.shape)   #for other Dimension array returns set of (rows,cols).

# Memory type:
print(a.dtype)
print(b.dtype)
# specify Memory type during array creation:
c=np.array([1,2,3,4],dtype='int16')
print(c)
print(c.dtype)

# Memory of each item:
print(c.itemsize)
print(a.itemsize)
print(b.itemsize)

# Total memory of array:
print(a.nbytes)
print(b.nbytes)
print(c.nbytes)

