# Basics of Lambda Functions:

# Lambda functions are Nameless or Anonymous Functions.

# Use:
 # 1-to reduce code size.
 # 2-Single time use.
 # 3-as I/P or O/P for Higher Order FUnctions.
 
# Syntax: lambda <args> : <expression>

# Examples: 

# to print square root of number:
x=lambda a : a*a
print(x(3))

# to print sum of 3 numbers:
y=lambda a,b,c : a+b+c
print(y(1,2,3))

# ------------------------------------------------------------------------------------------

# Anonymous Functions within  User Defined Functions:

def A(x):
    return (lambda y:x+y)
t=A(4)
print(t(6))
# here x=4 & y=6 to give result 10

p=A(10)
print(p(2))
# here x=10 & y=2 to give result 12
