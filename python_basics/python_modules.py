# import the math module, which contains features for working with mathematics
import math

# the math module contains lots of pre-built functions
def calculations():
    print("square root:",math.sqrt(16))
    print("power :",math.pow(2, 3))
    print("remainder :",math.remainder(100, 3))
    print("sine :",math.sinh(9.6))

# in addition to functions, some modules contain useful constants

def constants():
    print("PI:",math.pi)
    print("TAU:",math.tau)
    print("E:",math.e)
    print("NAN:",math.nan)
# try some of the math functions for yourself here:

def main():
    calculations()
    constants()

if __name__=="__main__":
    main()