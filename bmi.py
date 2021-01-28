# bmi.py
# calucates users bmi
# Author: Katie Mc Donald

# defining variables
name = input('Hello, what is your name? ')
height = float(input('{}, please enter your height in cm: '.format(name)))
weight = float(input('Now enter your weight in kilograms: '))

# BMI result
bmi = weight / (height/100)**2

print('{}, your BMI is {:.2f}'.format(name, bmi))