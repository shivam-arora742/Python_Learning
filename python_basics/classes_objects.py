#
# Example file for working with classes
#

# class definition:
class Myclass:
    def fn1(self):
        print("1st method called")
    
    def fn2(self,str):
        print("2nd method called with argument:"+str)

# 
# Python Inheritance:

class Base():
    def fn(self):
        print("base class")

class Derive(Base):
    def fn(self):
        Base.fn(self)
        print("Derive class")


# Python method overriding
# 
class D1(Base):
    def fn(self):
        print("over-riding method")

def main():
    # creation of object of class
    obj=Myclass()

    # object calling class methods:
    obj.fn1()
    obj.fn2(" hello world")
    
    #inheritance object
    c=Derive()
    c.fn() 

    # method overriding obj
    z=D1()
    z.fn()
if __name__ == "__main__":
      main()
