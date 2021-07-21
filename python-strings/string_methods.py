# String Methods:

name='shivam'
# 1-capitalize():capitalize first letter.
print(name.capitalize())

# 2-count():count the occurance of element.
print(name.count('a'))

# 3-find():find the position of element.
print(name.find('h'))

# 4-index():returns index of the element.
print(name.index('s'))

# 5-isalnum():check if string is alpha-numeric.
print(name.isalnum())

# 6-isalpha():check if string is alphabetic.
name='shivam123'
print(name.isalpha())

# 7-islower():check if string is in lower case.
 # -isupper():check if string is in upper case.
print(name.islower())
print(name.isupper())

# 8-lower():convert string  in lower case.
 # -upper():convert string  in upper case.
print(name.lower())
print(name.upper())

# 9-replace():replaces the element 1 by element 2.
print(name.replace('s','$'))

# 10-split():splits the entire string into parts based on element.
a='python is an easy language'
print(a.split('an'))

# 11-join():Join all items in a tuple into a string, using a hash character as separator:
mylist=['1','2','3']
print('-'.join(mylist))