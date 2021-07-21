# HackerRank-Python-String:

# Code:
def count_substring(string, sub_string):
    count=0             #to count occurance of sub_string in string:
    for i in range(0,len(string)):       #iterate in string
        if(string[i:i+len(sub_string)]==sub_string): #slice the string in columns and check if it equal to sub_string.
            count+=1
    return count

if __name__ == '__main__':