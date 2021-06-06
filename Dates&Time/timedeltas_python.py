#
# Example file for working with timedelta objects
#

# importing date,time,datetime &timedelta classes.
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# Python timedelta() function: is present under datetime library which is generally used for calculating differences in dates and also can be used for date manipulations in Python.

# construct a basic timedelta and print it
time_delta=timedelta(days=20,weeks=5,hours=5)
print(time_delta)

# print today's date
now=datetime.now()
print("today's date:",now)

# print today's date one year from now
print("One Year from now:",now+timedelta(days=365))

# create a timedelta that uses more than one argument
print("2days and 3 weeks from now :",now-timedelta(days=2,weeks=3))

# calculate the date 1 year and 3 weeks ago, formatted as a string
t=now-timedelta(days=365,weeks=3)
s=t.strftime("%A ,%d, %b ,%Y")
print("the date 1 year and 3 weeks ago :"+s)

### How many days until April Fools' Day?
today=date.today();
print(today)
# create a new date:
afd=date(today.year,4,1)
print(afd)

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if(afd<today):
    print("april fool's day already passed by days:",(today-afd).days)
    print("next year's april fool's day will be after :",today+timedelta(days=365)-afd)
 

