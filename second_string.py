# second_string.py
# This program takes an input of a string and outputs every second letter in reverse order.
# Author: Katie Mc Donald

# Getting the users input
string = input('Please enter a sentance: ')
print('You have entered: \n\t\t' + string)

# Reversing the order of the string. -1 is always the last value/element
reversed_string = string[::-1] # [starting value : end value : value to move by]
# Printing the second letter of the reversed string
print('Your new string is:\n\t\t'  + reversed_string[::2]) # [starting value : end value : value to move by]
