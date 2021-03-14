# pands-problem-sheet - Weekly Tasks
---

## Description
This is a ReadMe for the seven weekly tasks assigned for GMIT Diploma in Data Analytics' Programming and Scripting module.
The seven tasks are as follows:
        
        - bmi.py
        - second_string.py
        - collatz.py
        - weekday.py
        - squareroot.py
        - es.py
        - plottask.py

-- 

## bmi.py
The aim of this program is to take a users height in centimeters and weight in kilograms and calculate their Body Mass Index (BMI).
The formula to workout the BMI calculation is as follows; body weight divided by the square of the body height - kg/m². (NHS, 2021).
BMI is used to measure whether your weight is healthy. It has many limitations though such as it's inability to differenaiate between bone, fat and muscle.
I used the HSE's reference guide to identify the different weight categorys (HSE, 2021) and made this a clickable link in the program.
As the users height was inputted in centimeters, the program needed to change this to meters. It does this by diving by 100. As 100cm = 1m.
The example output in the task criteria was formatted to 2 decimal places hence the output of this program matches this.

'''
$python bmi.py

Hello, what is your name? Maeve
Katie, please enter your height in cm: 167
Now enter your weight in kilograms: 62

Katie, your BMI is 22.23.
Please refernce the following chart with your result to identify your category:

        - Underweight = < 18.5
        - Healthy Weight = 18.5–24.9
        - Overweight = 25-29.9
        - Obese Class I = 25–29.9
        - Obese Class II = 35-39.9
        - Obese Class III = > 40

For more information about BMI and weight management vist the HSE website at: https://tinyurl.com/6uvm5jr3
'''

## References
HSE. (2021). BMI Chart (Kgs/m2 ) for use with the Weight Management Treatment Algorithm. 
Available: https://www.hse.ie/eng/services/list/2/primarycare/east-coast-diabetes-service/management-of-type-2-diabetes/lifestyle-management/healthy-eating-advice/bmi-chart.pdf. Last accessed 14th March 2021.
NHS. (2021). What is the body mass index (BMI)?. 
Available: https://www.nhs.uk/common-health-questions/lifestyle/what-is-the-body-mass-index-bmi/. Last accessed 14th March 2021.
