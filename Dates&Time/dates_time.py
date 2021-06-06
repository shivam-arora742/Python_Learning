#
# Example file for working with date information
#

# 
# importing date,time,datetime classes from module:datetime
from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today=date.today()
  print(today)

  # print out the date's individual components
  print("Date components:",today.day," ",today.month," ",today.year)
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print("weekday index:",today.weekday())
  # accessing today's day of week.
  days=['mon','tues','wednes','thurs','fri','sat','sun']
  print("whats the day:",days[today.weekday()],"day")
  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  Current=datetime.now()
  print("Current Date and Time:",Current)
  
  # Get the current time
  print("Current Time:",datetime.time(datetime.now()))
 

  
if __name__ == "__main__":
  main();
  