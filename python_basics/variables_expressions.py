# 
# Example file for variables
#

# Declare a variable and initialize it
var =0
print("variable value: ",var)

# re-declaring the variable works
var="string"
print("variable value: ",var)

# ERROR: variables of different types cannot be combined
# example:
# print("hi"+12) 
# above code will throw error,then use str().
# 
print("hi "+str(12))


# Global vs. local variables in functions
# global variable :f
f=0
# function definition
def fn():
    # local variable :f
    # f="hello_world"

    # To make f as global variable:
    global f
    f="hello_world"
    print(f)

# function calling
fn()
print(f)

# Delete variable definition:
del f
print(f)
# Throws error because
#  definition of f is deleted 
#  and is now undefined.