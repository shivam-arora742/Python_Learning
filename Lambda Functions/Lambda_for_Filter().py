# Lambda functions within Filter():

# Filter(): filters out the elements from iterables(list,set)which gives
          # True or False to expression given in function passed as Argument.
        #   Syntax: list=filter(function,iterables)
        
# Using Lambda within Filter()to get even numbers from list:
mylist=[1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda a : (a%2==0),mylist))
print(even)

# Using Lambda within Filter()to get odd numbers from list:
mylist=[1,2,3,4,5,6,7,8,9,10]
odd=list(filter(lambda a : (a%2!=0),mylist))
print(odd)