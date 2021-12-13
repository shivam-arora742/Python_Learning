# # Data Types in Python:

# # Numeric Type:
#  # int:
# x=9
# print(type(x))

#  # float
# y=9.5
# print(type(y))

#  # bool:
# z=True
# print(type(z))

#  # complex:
# p=6+9j
# print(type(p))

#  # Conversions:
# a=float(x)
# b=complex(y,8)
# c=int(z)
# print(a,b,c)

# -----------------------------------------------------------------------------------
# # Sequence Data Types:

# # List:
# lst=[1,2,3,4]
# print(type(lst))
# print(lst)

# # Fetch elements by index:
# print(lst[2])
# print(lst[-2])

# # Slicing:
# print(lst[1:3])

# # Lists can hold numbers & strings as elements:
# miscellaneous=[1,'abc',2.5,'z']
# print(miscellaneous)

# # List Operations:
# # lists are mutables:append():
# lst.append(22)
# print(lst)
# # insert()
# lst.insert(1,99)
# print(lst)
# # remove():
# lst.remove(3)
# # pop()
# lst.pop(4)
# # extend():
# lst.extend([00,000])
# # sort():
# lst.sort()

# print(lst)

# # inbuild methods:
# print(min(lst))
# print(max(lst))

# -----------------------------------------------------------------------------------

# # Tuples:
# tup=(1,2,1,2,1,2)   #can have duplicate values
# print(tup)
# print(type(tup))

# # indexing & slicing:
# print(tup[0],tup[-1])
# print(tup[1:4])

# # Immutable in nature:
# a=(10,20,30,[1,2,3])
# # a[1]=22    #TypeError: 'tuple' object does not support item assignment
# a[3][2]=4
# print(a)

# # Concatenation:
# tup2=(1,2,3)
# tup3=(4,5,6)
# tup1=tup2+tup3
# print(tup1)

# # deleting tuple alltogether:
# del tup1
# # print(tup1)    #NameError: name 'tup1' is not defined

# # Tuple Methods:
# abc=(11,12,11,12,23,25,00)
# # count:
# print(abc.count(11))
# # index:
# print(abc.index(12))

# # Tuple COnstructor:
# lst=[1,2,3]
# tupl=tuple(lst)
# print(tupl)


# -----------------------------------------------------------------------------------

# # Sets:

# set1={1,2,3,4,'abc'}
# set2={'abc',2,4,99,100}
# print(set1,set2)

# # Add items:
# set1.add('efg')
# set1.update(['adfg',22,'ccc'])
# print(set1)

# # Remove items: 
# # set2.remove('efg')  #KeyError: 'efg'
# set2.discard('efg')
# print(set2)

# # Remove all items altogether:
# set2.clear()
# print(set2)
# set2=set(['efg','efg',1,1])
# print(set2)

# # Check item present in set:
# print('adfg' in set1)
# print('adfg' in set2)

# # Set operations:
# # union:
# print(set1.union(set2))
# # intersection:
# print(set1.intersection(set2))

# -----------------------------------------------------------------------------------

# Dictionary:
# empty dictionary:
dict1={}
print(dict1)
print(type(dict1))

# syntax:
dict2={1:'a',
       2:'b',
       3:'c',
       4:'d',
       5:'e',
       6:{'x':'y','p':'q'}}  #nested dictionary

print(dict2)

# fetch values by keys:
print(dict2[6])

# add new item:
dict2[7]='efgh'
print(dict2)

# remove item:
del dict2[3]
print(dict2)

#Dictionary methods:
# keys():
print(dict2.keys()) 
# items():
print(dict2.items())
# copy(): 
c=dict2.copy()
del c[1]
print(c)
# get():
print(dict2.get(4))
# update():
dict2.update({11:'abc',50:'qq'})
print(dict2)

# Dictionaries are mutable in nature:
dict2[1]='ef'
print(dict2)