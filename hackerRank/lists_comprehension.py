# Statement:Print the list in lexicographic increasing order (x,y,z) such that it is x+y+z!=n
# input x,y,z,n
x = int(input())
y = int(input())
z = int(input())
n = int(input())

#output list 
output=[]
# temporary list
abc=[]

#for loops for each order iteration 

for X in range(x+1):
    for Y in range(y+1):
        for Z in range (z+1):
            # if condition is true
            if(X+Y+Z!=n):
                #add ordered pair to temporary list 
                abc=[X,Y,Z]
                # # append the output list
                output.append(abc)
# print output
print(output)