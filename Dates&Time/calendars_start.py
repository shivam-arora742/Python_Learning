#
# Example file for working with Calendars
#

#Python defines an inbuilt module calendar which handles operations related to calendar. 
# import the calendar module

import calendar

# calendar of given month:
month=3;
year=2020;
print("Calendar of month:",calendar.month(year,month))

# calendar of given year:
# parameters:year,width(btw columns),line(btw rows),c(space btw mnths),m(no.of mnths in each row).
print(calendar.calendar(2021,2,1,2,6))


# create a plain text calendar

# TextCalendar class->generates plain text calnedar with parameter->calendar.weekday(starting day).
c=calendar.TextCalendar(calendar.MONDAY)
# formatmonth()method used to generate calendar of given month.
# parameters: yr,mnth,width,line.
str=c.formatmonth(2021,5,5,2)
print(str)

# create an HTML formatted calendar
hc=calendar.HTMLCalendar(calendar.SUNDAY)
str1=hc.formatmonth(2021,5)
print(str1)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2021,5):
    print(i)
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms

# to get month names:
for mnth in calendar.month_name:
    print(mnth)

# to get weekday names:
for day in calendar.day_name:
    print(day)


# Exercise:

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:


# Answer:
# print ("Team meetings will be on:")
# for m in range(1,13):
#   # returns an array of weeks that represent the month
#   cal = calendar.monthcalendar(2017, m)
#   # The first Friday has to be within the first two weeks
#   weekone = cal[0]
#   weektwo = cal[1]
   
#   if weekone[calendar.FRIDAY] != 0:
#     meetday = weekone[calendar.FRIDAY]
#   else:
#     # if the first friday isn't in the first week, it must be in the second
#     meetday = weektwo[calendar.FRIDAY]
      
#   print ("%10s %2d" % (calendar.month_name[m], meetday))
