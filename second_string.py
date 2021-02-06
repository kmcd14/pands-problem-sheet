# second_string.py
# weekly task03
# a program that takes asks a user to input a string and outputs every second letter in reverse order.
# author: Katie Mc Donald

string = input('Please enter a sentance: ')
print('you have entered: \n' + string)

# reversing the order of the string. -1 is always the last value/element
# [starting value : end value : value you wish to move by]
reversed_string = string[::-1]

# printing the second letter of the reversed string
print('your new string is:\n'  + reversed_string[::2])
