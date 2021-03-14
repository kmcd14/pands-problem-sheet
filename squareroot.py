# squareroot.py
# This program takes a positive floating-point number as input and outputs an approximation of its square root using the Newton Method
# Author: Katie Mc Donald

# Defining a function that uses Newton's Method
def sqrt(number):
    approx_root = number / 2  # Guessing the approx root estimate of the number
    # While the following conditions are true do the following
    while True: # Main loop
        # Add the approx root to the (number divided approx root) divided by 2 
            better_guess = ((approx_root + (number / approx_root)) /2)  # gradually improving intial guess estimate
            # If the improved guess is equal to the approx guess beak out of the loop
            if better_guess == approx_root:
                # rounding to one decimal place to match example output given in task description 
                print('Using Newtons Method we estimate the squareroot of {} to be {:.1f}'.format(number_to_root, better_guess))
                break 
            # Reassigning approx root
            approx_root = better_guess
    

# Getting the users input as a float
number_to_root= float(input('Please enter a posistive number: ' ))
# Calling function   
sqrt(number_to_root)
