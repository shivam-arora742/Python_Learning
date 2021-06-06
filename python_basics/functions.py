#
# Example file for working with functions
#

# define a basic function
def f1():
    print("I am a Function")

# function that takes arguments
def arg(arg1,arg2):
    print(arg1," ",arg2)
# function that returns a value
def square(x):
    return x*x

# function with default value for an argument
def power(num,x=1):
    output=1
    for i in range(x):
        output*=num
    return output

#function with variable number of arguments
def multi_add(*args):
    result=0
    for i in args:
        result+=i
    return result



# simple calling a function
f1()
# passing the function as object to print and execute the function statements and return none. 
print(f1())
# throws error because of invalid syntax
print(f1)

# function that takes or return some value.
arg(10,20)
print(arg(10,20))
print(square(10))

# Default argument function.
print(power(2))
print(power(2,3))
# on swapping the order of arguments but providing them name:
print(power(x=3,num=2))
# python interpreter will figure out the values corresponding to the argument .

# multiple arguments :
print(multi_add(1,2,3,4,5))