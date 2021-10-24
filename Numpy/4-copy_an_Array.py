# Be carefull when copying an array:

# Import numpy
import numpy as np;

# # Direct assigning one array to  another:
# a=np.array([1,2,3])
# b=a
# b[0]=99
# print(b)
# print(a) 

# Problem arises: when modifying element of array 'b' , element of array 'a' also gets modified.
# Reason: 'b' array points to the same data space as array 'a' is pointing, 
        # hence modifying one may leads to modification of original array. 
        

# By using copy() method.
a=np.array([1,2,3])
b=a.copy()
b[0]=99
print(b)
print(a) 

# Reason: in matrix 'b' , a copy of 'a' matrix is passed.