# Numpy STatistics:(mean,median,mode,max ......)

import numpy as np
stats=np.array([[1,2,3],[4,5,6]])


# Min & MAx of matrix:
print(stats.min())  
print(stats.max())  

# sum of matrix:
print(np.sum(stats))

# mean(average)of matrix:
print(stats.mean())

# median of matrix:
print(np.median(stats))

# variance of matrix:
print(np.var(stats))

# standard deviation:
print(np.std(stats))