# The functions isupper() and islower() returns the boolean True value if the all the characters of the string are in upper case or lower case respectively.

# The functions upper() and lower() returns the string by converting all the characters of the string to upper case or lower case respectively

def swap_case(s):
    output=""
    for char in s:
        if(char.islower()==True):
            output+=char.upper()
        elif(char.isupper()==True):
            output+=char.lower()
        else:
            output+=char
    return output

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)