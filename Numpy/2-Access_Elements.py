# import numpy:
import numpy as np;

# 2-D array:
a=np.array([
    [ 1, 2, 3, 4,  5],
    [ 6, 7, 8, 9, 10]
])
print(a)
print(a.shape)

# Get specific element:
# array indexing starts from 0 to n-1.
print(a[1,3])
print(a[0,2])
# using negative indexing:
print(a[1,-1])

# Get a specific row:
print(a[0,:])
print(a[1,:])


# Get a specific column:
print(a[:,0])
print(a[:,3])

# Array Slicing:
print(a[0,1:4:1])
print(a[1,::2])

# Modifying an Element:
a[0,2]=99
print(a)

# Modifying a Row:
a[0,:]=0
print(a)

# Modifying a col:
a[:,2]=[10,99]
print(a)