#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 
  
  now=datetime.now()
  print(now)
  
  #### Date Formatting ####
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
  
  print(now.strftime("Current day: %a"))
  print(now.strftime("Current day: %A"))
  print(now.strftime("Current month: %b"))
  print(now.strftime("Current month: %B"))
  print(now.strftime("Current year: %y"))
  print(now.strftime("Current year: %Y"))
  print(now.strftime("Current day of month: %d"))
  print(now.strftime("Week number of year: %W"))
  print(now.strftime("Day number of year: %j"))


  # %c - locale's date and time, %x - locale's date, %X - locale's time
 
  print(now.strftime("local date:%x"))
  print(now.strftime("local time:%X"))
  print(now.strftime("local date and time:%c"))

  #### Time Formatting ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
 
  print(now.strftime("24 hour clock time-%H:%M:%S"))
  print(now.strftime("12 hour clock time-%I:%M:%S %p"))

  # Exercise:
  print(now.strftime("%Y - %d,%X - %c"))

if __name__ == "__main__":
  main();
