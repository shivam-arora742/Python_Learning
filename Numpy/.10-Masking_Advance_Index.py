# # Boolean masking and Advance Indexing:

import numpy as np

# filedata=np.genfromtxt('test.txt', delimiter=',')
# filedata=filedata.astype('int32')

# # check for all filedata items >50:
# print(filedata>50)

# # to get array of filedata elements >50:
# print(filedata[filedata > 50])    #takes only that element returns true for condition(filedata > 50)

# # numpy indexing with a list:
# a=np.array([1,2,3,4,5,6,7,8,9,0])

# print(a[[1,3,5,7,9]])   #passing index list to gather element.

# # check if any filedata is greater than 50:
# print(np.any(filedata > 50,axis=0))    
# # axix=0 for row (x-axis))
# # axix=1 for col (y-axis)

# # Negation conditon:
# print(~(filedata>50))

# --------------------------------------------------------------------------------------------------

# Practice Question:
# A=  1  2  3  4  5
#     6  7  8  9  10
#     11 12 13 14 15
#     16 17 18 19 20
#     21 22 23 24 25
#     26 27 28 29 30

A=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]])
print(A)

# task-1: get  elements :11 12
                        # 16 17
print(A[2:4,0:2])


# task-2: get elements:   2
                        #   8
                            #  14
                            #     20 
                            
print(A[[0,1,2,3],[1,2,3,4]])


# task-3: 4    5
        # 24   25
        # 29   30
print(A[[0,4,5],3:])
