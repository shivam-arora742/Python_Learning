# Initialization of Different Types of Arrays:

# import numpy:
import numpy as np

# # All zero's (0's) matrix:
 
#  # 1-D array:
# a=np.zeros(4)
# print(a)

#  #2-D array:
# b=np.zeros((2,5))
# print(b)

# # 3-D array:
# c=np.zeros((2,3,5))
# print(c)


# # All 1's matrix:
# d=np.ones((2,3),dtype='int64')
# print(d)


# # Matrix with any other number:
# e=np.full(4,1000)
# print(e)

# # Reusing exisiting matrix :
# f=np.full_like(b,5)
# print(f)

# # Matrix with random decimal number:
# xyz=np.random.rand(3,5)
# print(xyz)

# # Matrix with random integer number:
# abc=np.random.randint(10,size=(2,2))
# print(abc)

# # Identity matrix:(Square matrix)
# id=np.identity(2)
# print(id)

# Practice Question:
# Matrix:    1 1 1 1 1
          #  1 0 0 0 1
          #  1 0 9 0 1
          #  1 0 0 0 1
          #  1 1 1 1 1
          
# Steps:
# 1-make an all 1's matrix of 5x5.
output=np.ones((5,5))
print(output)

# 2-make tmp array of all 0's of 3x3.
tmp=np.zeros((3,3))
print(tmp) 

# 3-make elemnt at (1,1) in tmp as 9.
tmp[1,1]=9
print(tmp) 

# 4-replace middle part of output matrix with tmp:
output[1:4,1:4]=tmp
print(output)