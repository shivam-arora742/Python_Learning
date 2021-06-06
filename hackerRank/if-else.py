# Statement:Print Weird if the number is weird. Otherwise, print Not Weird.
# n=24
n=3
if(n%2!=0):
    print("Weird")
elif(n%2==0):
    if(n>=2 and n<=5):
        print("Not Weird")
    elif(n>=6 and n<=20):
        print("Weird")
    elif(n>20):
        print("Not Weird")