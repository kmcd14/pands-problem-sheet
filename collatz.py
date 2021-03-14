# collatz.py
# This program takes the input of a positive integer  and calculates the
# next value by taking the current value and if it is even \ 2. if odd * 3 + 1 
# The program will end if the current value is one.
# Author: Katie Mc Donald


# creating a function
def collatz(number):
    # main loop
     while True:  # while the following conditions are true do the following
            # finds if it's an even number (i.e. no remainder)                     
            if (number % 2) == 0:  
                new_number = number / 2
                # prints new value of number.
                print(int(new_number)) # Added int() as it was printing out a float otherwise   
             # finds if it's an odd number (i.e. has a remainder)
            elif (number % 2) == 1:   
                new_number = (number * 3) + 1
                # prints new value
                print(int(new_number)) 
            # reassigns the value of number. Without this the first result is printed on an infinite loop
            number = new_number 
            # breaks out of the loop when 1 is reached
            if new_number == 1:          
                break 


# defining a variable from user input and changing the string into an integer 
user_number = int(input('Please enter a posistive integer: '))
# calls the function
collatz(user_number)
print(collatz) 