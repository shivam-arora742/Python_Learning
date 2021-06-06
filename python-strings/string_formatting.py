# String Interpolation and Formatting:

a='shivam'
b='arora'
c=20

# String Interpolation& Formatting techniques:
# 
#1-%s technique:substituting the value of strings. 
print("I am %s %s living in MP."%(a,b))
print("I am currently %s years old."%(c))

# 2-f{} technique:
print(f"Hello,I am {a} {b},currently {c} years old.")

# 3-str.format():
name="shivam"
full_name="{name} arora".format(name=name)
print(full_name)