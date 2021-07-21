# HACKER-RANK-PYTHON-STRINGS:

# Question Description:
# Complete the split_and_join function in the editor below.

# split_and_join has the following parameters:

# string line: a string of space-separated words
# Returns

# string: the resulting string
# Input Format
# The one line contains a string consisting of space separated words.

# Sample Input
# this is a string
#    
# Sample Output
# this-is-a-string

# Code:
def split_and_join(line):
    # write your code here
    x=line.split(" ")          #split the line with " " and store in x.
    y="-".join(x)              #join the x string with hash character as '-'.
    return y                   #return modified string.

if __name__ == '__main__':