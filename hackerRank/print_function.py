# Problem Statement:Print the list of integers from 1 through n as a string, without spaces.
n = input()
n=int(n)
# range will print number from 1 to n,excluding n+1
for i in range(1,n+1):
    # this statement will print value of i and ends with ''(blank).
    print(i,end='')