# weekday.py
# This program tells the user whether or not today is a weekday.

 # Importing module that allows the manipulation of dates and times
import datetime 
# This method assigns a number to the days of the week 
# Mon = 0, Tues = 1, Wed = 2, Thurs = 3, Fri = 4, Sat = 5, Sun = 6
day_of_week = datetime.datetime.today().weekday() # Assigning day to a variable 

# Defining a function
def weekday(day):
    # If today is less than or equal to 4 (i.e. Monday - Friday) it's a weekday.
    if day <= 4: 
        print('Yes, today is a weekday :( ')
    else: # Otherwise it's the weekend (i.e. Saturday - Sunday)
        print("WooHoo! It's the weekend! :)")

# Calling the function
weekday(day_of_week)