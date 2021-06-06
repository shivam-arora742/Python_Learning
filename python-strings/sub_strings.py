# In python,substrings are a portion of string.
# it is also reffered as string slicing.

# substring syntax: string[start:end]
name="hello world is the first word in programmer's life!!!"
print(name[0:5])    #to access substring "hello".
print(name[33:43])  #to access substring "programmer".

# optional step index:
print(name[0:5:3])    #substring with stepping forward: 3.
print(name[0:5:1])    #default step index is :1.

# reversing a string using slicing method:
print(name[::-1])
print(name[-1::-1])

# negative indexing substring:
name="hello"
print(name)
print(name[-2:-1])
print(name[-2:])

# we cant back propogate in strings.