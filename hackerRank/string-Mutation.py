# Hacker-Rank-Python-String:

# Question Description:
# Complete the mutate_string function in the editor below.

# mutate_string has the following parameters:

# string string: the string to change
# int position: the index to insert the character at
# string character: the character to insert
# Returns

# string: the altered string
# Input Format
# The first line contains a string, .
# The next line contains an integer , the index location and a string , separated by a space.

# Sample Input
# STDIN           Function
# -----           --------
# abracadabra     s = 'abracadabra'
# 5 k             position = 5, character = 'k'

# Sample Output
# abrackdabra

# Code:
def mutate_string(string, position, character):
    x=string[:position]                  #slice string from 0 to pos .
    y=string[position+1:]                #and from pos+1 to end .
    return x+character+y                 #concatenate all substrings and return .

if __name__ == '__main__':