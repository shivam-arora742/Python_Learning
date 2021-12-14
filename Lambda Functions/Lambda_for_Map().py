# Lambda FUnction within Map():

# Map(): used to apply function condition on all iterable items & 
       # return list of boolean values.
    #    Syntax: map(function,iterables).
    
# Lambda within Map():
l=[1,2,3,4,5,6]
p=list(map(lambda x : (x%2!=0),l))
print(p)

