#Program-1:hello_world.
# Example file for HelloWorld
#
# print():used to display output.
# input():used to take some input.
# 
# print("hello_world!!")
# name=input("What is your name?")
# print("nice to meet you, ",name)
# 
# python function:
def fn():
    print("hello_world!!")
    name=input("What is your name?")
    print("nice to meet you, ",name)

# check for main() and executing it.
if __name__=="__main__":
    fn()
# So when the interpreter runs a module, the __name__ variable will be set as  __main__ if the module that is being run is the main program.
# But if the code is importing the module from another module, then the __name__  variable will be set to that module’s name.
