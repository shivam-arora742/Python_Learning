# ReOrganising Arrays in Numpy:

import numpy as np

# Reshaping array:

# before array:
before =np.array([[1,2,3,4],[5,6,7,8]])
print(before)
print(before.shape)

# Reshape 'before'  array to (4,2):
after=before.reshape((4,2))
print(after)
print(after.shape)



# Vertical Stacking of Matrices: 

v1=np.array([1,2,3,4])
print(v1)
v2=np.array([5,6,7,8])
print(v2)

# combining matrices vertically:
res=np.vstack([v1,v2])
# res=np.vstack([v1,v2,v1,v2])
print(res)



# Horizontal Stacking of Matrices:

h1=np.ones((2,2))
print(h1)
h2=np.zeros((2,2))
print(h2)

result=np.hstack([h2,h1])
print(result)


# 