def is_leap(year):
    leap = False
    # if it is century year (00)
    if(year%100==0 and year%400==0):
        leap=True 
    if(year%100!=0 and year%4==0):
        leap=True
    return leap
year=input()
year=int(year)
print(is_leap(year))
