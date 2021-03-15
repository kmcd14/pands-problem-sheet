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

$python bmi.py
'''
Hello, what is your name? Maeve
Maeve, please enter your height in cm: 167
Now enter your weight in kilograms: 62

Maeve, your BMI is 22.23.
Please refernce the following chart with your result to identify your category:

        - Underweight = < 18.5
        - Healthy Weight = 18.5–24.9
        - Overweight = 25-29.9
        - Obese Class I = 25–29.9
        - Obese Class II = 35-39.9
        - Obese Class III = > 40

For more information about BMI and weight management vist the HSE website at: https://tinyurl.com/6uvm5jr3
'''

## second_string.py
The goal of this program is to take an input of a string and print out every second letter in reverse order.
To achieve this I used slicing. The slice method takes three arguments; [starting value : end value : value to move by] (W3Schools, 2021)
Since the objective is reverse the full string we don't have to enter specfic start and end values. 
-1 will always be the last value. By adding it as the third arguments the program will read the string backwards.
The second part of the task was to output every second letter of the reversed string.
To achieve this we use slicing again. On the newly revered string we pass 2 as the third arguments. 
The program will move through the revered string and print every second letter


$python second_string.py
    '''
    Please enter a sentance: this is an example
    You have entered:
                    this is an example
    Your new string is:
                    epaen ish
    '''

## collatz.py
This program asks the user to input a positive integer and will output the successive values of the following calculation. The program will calculate the next value by taking the current value and, if it even, divide it by two, but if odd, multiply it by three and add one. It will continue this calculation until the value is one. 
The task description didn't specify putting the code into a function, I decided to do this after learning about them in week 6.
The name of the program in the task description lead me to researching the collatz sequence also know as Collatz conjecture, was purposed by German mathematician Lothar Collatz. The formula states "... that any orbit for the iteration function f (n) = (3n + 1)/2, for n odd, and f (n) = n/2, for n even, is always attracted to the value 1." (J.F. Alves et. al., 2005). That is all posistive integers used in this process it will eventually converge to one. To date it is still considered unsolved (Hartnett, 2019).
         '''
        $ python .\collatz.py
        Please enter a posistive integer: 12
        6
        3
        10
        5
        16
        8
        4
        2
        1
        '''

## weekday.py
This program tells the user whether or not today is a weekday.
Modules used for this program are datetime. "The datetime module supplies classes for manipulating dates and times." (Python, 2021)
        import datetime
The two methods the program uses are 
- today() this method gets the current date
- weekday() this method returns the days as an integer: Monday = 0, Tuesday = 1, Wednesday = 2, Thursday = 3, Friday = 4, Saturday = 5, Sunday = 6 (Python, 2021)
Using this I was able to create a simple function where if todays date is <= 4 it's a weekday, otherwise it's the weekend.
        '''
        $python weekday.py
        Yes, today is a weekday :(
        '''



## References
Hartnett, Kevin. (2019). Mathematician Proves Huge Result on ‘Dangerous’ Problem. Available: https://www.quantamagazine.org/mathematician-terence-tao-and-the-collatz-conjecture-20191211/. Last accessed 15th March 2021.
HSE. (2021). BMI Chart (Kgs/m2 ) for use with the Weight Management Treatment Algorithm. 
Available: https://www.hse.ie/eng/services/list/2/primarycare/east-coast-diabetes-service/management-of-type-2-diabetes/lifestyle-management/healthy-eating-advice/bmi-chart.pdf. Last accessed 14th March 2021.
J.F. Alves, M.M. Graça, M.E. Sousa Dias∗ , J. Sousa Ramos. (2005). A linear algebra approach to the conjecture of Collatz. Linear Algebra and its Applications. 394 (0), p277-278.
NHS. (2021). What is the body mass index (BMI)?.Available: https://www.nhs.uk/common-health-questions/lifestyle/what-is-the-body-mass-index-bmi/. Last accessed 14th March 2021.
Python. (2021). datetime — Basic date and time types. Available: https://docs.python.org/3/library/datetime.html. Last accessed 15th March 2021.
W3Schools. (2021). Python slice() Function. Available: https://www.w3schools.com/python/ref_func_slice.asp. Last accessed 14th March 2021.
