# Lambda within Reduce():

# Reduce():applies function condition to given iterables and return single value as O/p.
        #  syntax: reduce(fn,iterables).
  
#to import reduce:
from functools import reduce
   
#Lambda within Reduce:
p=reduce(lambda x,y : x+y,[1,2,3,4,5,6])
print(p)