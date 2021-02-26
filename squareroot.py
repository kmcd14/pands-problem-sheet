# squareroot.py
# This program takes a positive floating-point number as input and outputs an approximation of its square root.
# Newton Method:
# Guess the approx root estimate of the number
# Add the approx root to the (number divided approx root) divided by 2 
# Author: Katie Mc Donald

number_to_root= float(input('Please enter a posistive number: ' ))


# Define the function that uses Newton's Method
def sqrt(number):
    guess = number / 2  # getting an approx first root
    while True:
            better_guess = ((guess + (number / guess)) /2)  # gradually improving intial guess estimate
            if better_guess == guess:
                # rounding to one decimal place to match example output given in task description 
                print('Using Newtons Method we estimate the squareroot to be {:.1f}'.format( better_guess))
                break 
            guess = better_guess
    
sqrt(number_to_root)
