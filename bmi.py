# bmi.py
# This program takes in the users height in cm and weight in kilograms
# and use these inputs to calucate and output the users BMI
# Author: Katie Mc Donald


# defining variables from users input 
name = input('Hello, what is your name? ')
# changing the input value from a string to a float values
height = float(input('{}, please enter your height in cm: '.format(name)))
weight = float(input('Now enter your weight in kilograms: '))

# formula to calculate BMI is kg/m2 
bmi = weight / (height/100)**2  # changing cm into meters. dividing by 100 because 1m = 100cm

# .2f formats value returned to 2 decimal places. The example output in the Task critera was formatted like this
print('\n{}, your BMI is {:.2f}.\nPlease refernce the following chart with your result to identify your category: '.format(name, bmi)) 
print('\n\t- Underweight = < 18.5\n\t- Healthy Weight = 18.5–24.9\n\t- Overweight = 25-29.9\n\t- Obese Class I = 25–29.9\n\t- Obese Class II = 35-39.9\n\t- Obese Class III = > 40') 
# adding a clickable hyperlink to the HSE website
hse_link = 'https://tinyurl.com/6uvm5jr3'
print('\nFor more information about BMI and weight management vist the HSE website at: {}'.format(hse_link))