#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  while(x<5):
        if(x%2==0):
              print(x," :even")
        else :
              print(x," :odd")
        x+=1
    
  # 
  # define a for loop(used for iteration)
  for i in range(5):
        print(i)
  # 

  # use a for loop over a collection
  days=['mon','tues','wednes','thurs','fri','sat','sun']
  for d in days:
    print(d)  
  
  # 
  # use the break and continue statements
  for a in range(2,10):
        if(a==4): break
        print(a) 
  
  z=1
  while(z<10):
        if(z%2==0): 
          z=z+1 
          continue
        print(z)
        z+=1

  #using the enumerate() function to get index 
  # 
  char=["a","b","c","d","e"]
  for indx,c in enumerate(char):
    print(indx,":",c)

if __name__ == "__main__":
  main()
