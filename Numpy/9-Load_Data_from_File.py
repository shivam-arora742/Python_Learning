# Load data from file 'test.txt' in an Array using Numpy:

import numpy as np

# getting data from text file into an array:
output=np.genfromtxt('test.txt',delimiter=',')

print(output) 
# all the data are in float type:


# to load data as integer type:
output=output.astype('int32')
print(output)