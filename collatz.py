# collatz.py
# This program asks the user to input any positive integer 
# It will calculate next value by taking the current value
# if it is even, divide it by two, but if odd, multiply it by three and add one.
# The program will end if the current value is one.
# Author: Katie Mc Donald


number = int(input('Please enter a posistive integer: '))
new_number = 0

while True:                              # while the following conditions are true do the following
        if (number % 2) == 0:            # finds if it's an even number (no remainder)
            new_number = number / 2
            print(int(new_number))       
        elif (number % 2) == 1:           # finds if it's an odd number
            new_number = (number * 3) + 1
            print(int(new_number)) 
        
        number = new_number
        
        if new_number == 1:                # breaks out of the loop when 1 is reached
            break
