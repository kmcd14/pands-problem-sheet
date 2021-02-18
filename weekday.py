# weekday.py
# # Weekly Task 05
# This program will outputs whether or not today is a weekday.

import datetime 
# this function assigns an int to the days of the week 
# Mon = 0, Tues = 1, Wed = 2, Thurs = 3, Fri = 4, Sat = 5, Sun = 6
day_of_week = datetime.datetime.today().weekday()

# if today is less than or equal to 4
# i.e. Mon - Fri 
if day_of_week <= 4:
    print('Yes, today is a weekday :( ')
# otherwise it's the weekend
else:
    print("WooHoo! It's the weekend! :)")
