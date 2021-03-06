<br>
<h1 style=color:#DDA0DD><b><u> pands-problem-sheet - Weekly Tasks</b></u></h1>

---
</br>
<h3 style=color:#DDA0DD><b><u>Description</b></u></h3>
This is a ReadMe for the seven weekly tasks assigned for GMIT Diploma in Data Analytics, Programming and Scripting module.

---

<br>
<h3 style=color:#DDA0DD><b><u>Table of Contents</b></u></h3></summary>
  <ol>
    <li><a href="#bmi.py"> Week 02 - bmi</a></li>
    <li><a href="#second_string">Week 03 - second_string</a></li>
    <li><a href="#collatz.py">Week 04 - collatz</a></li>
    <li><a href="#weekday.py">Week 05 - weekday</a></li>
    <li><a href="#squareroot.py">Week 06 - squareroot</a></li>
    <li><a href="#es.py">Week 07 - es</a></li>
    <li><a href="#plottask.py">Week 08 - plottask</a></li>
    <li><a href="#Technologies_Used">Technologies Used</a></li>
    <li><a href="#References">References</a></li>
  </ol>
  
---
---
<br>
<h2 style=color:#B0E0E6><b><u><p id="bmi.py"> Week 02 - bmi.py</b></u></p></h2>
The aim of this program is to take a users height in centimeters and weight in kilograms and calculate their Body Mass Index (BMI).

BMI is used to measure whether your weight is healthy. It has many limitations though such as it's inability to differenaiate between bone, fat and muscle.
The formula to workout the BMI calculation is as follows; body weight divided by the square of the body height - kg/m². (NHS, 2021).

I used the HSE's reference guide to identify the different weight categorys (HSE, 2021) and made this a clickable link in the program.
As the users height was inputted in centimeters, the program needed to change this to meters. It does this by diving by 100. As 100cm = 1m.
The example output in the task criteria was formatted to 2 decimal places hence the output of this program matches this.
```
      $python bmi.py

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
```
---
</br>
<br>
<h2 style=color:#B0E0E6><b><u><p id="second_string">Week 03 - second_string.py</b></u></p></h2>
The goal of this program is to take an input of a string and print out every second letter in reverse order.
To achieve this I used slicing. The slice method takes three arguments; [starting value : end value : value to move by] (W3Schools, 2021)
Since the objective is reverse the full string we don't have to enter specfic start and end values. 
-1 will always be the last value. By adding it as the third arguments the program will read the string backwards.
The second part of the task was to output every second letter of the reversed string.
To achieve this we use slicing again. On the newly revered string we pass 2 as the third arguments. 
The program will move through the revered string and print every second letter

```
      $python second_string.py
          
      Please enter a sentance: this is an example
      You have entered:
                      this is an example
      Your new string is:
                      epaen ish
```

---
</br>
<br>
<h2 style=color:#B0E0E6><b><u><p id="collatz.py">Week 04 - collatz.py</b></u></p></h2>
This program asks the user to input a positive integer and will output the successive values of the following calculation. The program will calculate the next value by taking the current value and, if it even, divide it by two, but if odd, multiply it by three and add one. It will continue this calculation until the value is one. 
The task description didn't specify putting the code into a function, I decided to do this after learning about them in week 6.

The name of the program in the task description lead me to researching the collatz sequence also know as Collatz conjecture, was purposed by German mathematician Lothar Collatz. The formula states "... that any orbit for the iteration function f (n) = (3n + 1)/2, for n odd, and f (n) = n/2, for n even, is always attracted to the value 1." (J.F. Alves et. al., 2005). That is all posistive integers used in this process it will eventually converge to one. To date it is still considered unsolved (Hartnett, 2019).

  ```
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
```
---
</br>
<br>
<h2 style=color:#B0E0E6><b><u><p id="weekday.py">Week 05 - weekday.py</b></u></p></h2>
This program tells the user whether or not today is a weekday.
Modules used for this program are datetime. "The datetime module supplies classes for manipulating dates and times." (Python, 2021)

 ```
    import datetime
 ```
The two methods used from this module are: 
- today() this method gets the current date
- weekday() this method returns the days as an integer: Monday = 0, Tuesday = 1, Wednesday = 2, Thursday = 3, Friday = 4, Saturday = 5, Sunday = 6 (Python, 2021).

Using this I was able to create a simple function where if todays date is <= 4 it's a weekday, otherwise it's the weekend.
      
```
    $python weekday.py
    Yes, today is a weekday :(
```
---
</br>
<br>
<h2 style=color:#B0E0E6><b><u><p id="squareroot.py">Week 06 - squareroot.py</b></u></p></h2>
This program takes a positive floating-point number as input and outputs an approximation of its square root without using one of pythons built in math functions. I approached this problem by using the Newton Method. The algorithm for the Newton method is:

 1) Take a resonable guess at the appoximate root of the number
 2) Add this approximate root to the orignal number and divide by two (x_i := (x_i + n / x_i) / 2)
 3) Repeat step 2 until a percise value is reached. (Regmi, 2020)
 The output is a float with one point after the decimal to match the output in the task description. 

```
    $python squareroot.py
    Please enter a posistive number: 14.5
    Using Newtons Method we estimate the squareroot of 14.5 to be 3.8
  ```
---
</br>
<br>
<h2 style=color:#B0E0E6><b><u><p id="es.py">Week 07 - es.py</b></u></p></h2>
This program reads in a text file and outputs the number of times 'e' appears. It will take a filename from an argument on the command line.
The module used for this program is sys. This module "... provides access to any command-line arguments via the sys.argv."(Tutorials Point, 2021). I gave the filename variable the argument[1] as the script name is [0].

``` 
    import sys
``` 

The program opens the text file in read mode and iteriates though each line counting the number of times 'e' appears. I used 
  
  ``` 
      with open(filename, 'r') as f:
  ```

as it means the file is automatically closed, thus, reducing the chance of an error. 
The two methods the program uses are: 
- strip() this method gets rid of any whitespace at the start and end of the text.
- lower() this method converts all letters into lowercase. I did this so capitalized 'E' would be inculded in the count.

 ```
    $python es.py test.txt
    23
```
</br>

---
<br>

<h2 style=color:#B0E0E6><b><u><p id="plotask.py">Week 08 - plottask.py</b></u></p></h2>
This program displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
Modules used in this program are numpy and matplotlib
        import numpy as np
        import matplotlib.pyplot as plt
To find which points to plot I used numpy. "NumPy is the fundamental Python library for numerical computing." (Stojiljković, 2021). The program passes the range [0, 4] to create a numpy array. NumPy arrays are prefered to a list as they are faster and more efficient than python lists  (NumPy, 2021). 
I referenced the documentation on matplotlib to style and format the plot (Hunter, J., et. al., 2021). 

The methods the program uses are: 
- np.array() creates a numpy array from the range passed to it
- plt.plot() plots the functions
- plt.xlabel() and .ylabel() adds labels to the X and Y axes
- plt.title() adds a title to the  plot
- plt.legend() adds a legend to the plot 
- plt.grid() adds a grid to the plot
- plt.xticks() and .yticks() adds ticks along the X and Y axes
- plt.show() shows the plot when the program is run. I used this instead of save as the task description didn't state to save the plot.

 <img src='plottask_output.png'>
</br>

<br>

---
---
<h2><b><u><p id='Technologies_Used'> Technologies Used:</b></u></p></h2>



<b><u>Google Docs:</u></b> an online word processor used to write my documentation before transfering into this README file. https://www.google.com/docs/about/

<b><u>Anaconda:</u></b> the easiest way to perfrom Python data science machine learning on Windows, Linux and Mac OS. These programs where created using Version 4.9.2. https://www.anaconda.com/distribution/

<b><u>Python:</u></b> an interpreted, object-oriented, high-level programming language with dynamic semantics. This programs where created using Version 3.8.5.  https://www.python.org/

<b><u>Visual Studio Code:</u></b> An open source coding editor. https://code.visualstudio.com/

<b><u>GitHub:</u></b> is a code hosting platform for collaboration and version control. https://github.com/

---
---
</br>

<h1 style=color:#DDA0DD><b><u><p id="References"> References</b></u></p></h1>
Alves, J., Graça, M., Dias, M., Ramos, J. (2005). A linear algebra approach to the conjecture of Collatz. Linear Algebra and its Applications. 394 (0), p277-278.

Hartnett, Kevin. (2019). Mathematician Proves Huge Result on ‘Dangerous’ Problem. Available: https://www.quantamagazine.org/mathematician-terence-tao-and-the-collatz-conjecture-20191211/. Last accessed 15th March 2021.

HSE. (2021). BMI Chart (Kgs/m2 ) for use with the Weight Management Treatment Algorithm. 
Available: https://www.hse.ie/eng/services/list/2/primarycare/east-coast-diabetes-service/management-of-type-2-diabetes/lifestyle-management/healthy-eating-advice/bmi-chart.pdf. Last accessed 14th March 2021.

Hunter, J., Dale, D., Firing, E., Droettboom, M., et al. (2021). matplotlib.pyplot.plot. Available: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html. Last accessed 15th March 2021.

NHS. (2021). What is the body mass index (BMI)?.Available: https://www.nhs.uk/common-health-questions/lifestyle/what-is-the-body-mass-index-bmi/. Last accessed 14th March 2021.

NumPy. (2021). NumPy: the absolute basics for beginners. Available: https://numpy.org/doc/stable/user/absolute_beginners.html. Last accessed 15th March 2021.

Python. (2021). datetime — Basic date and time types. Available: https://docs.python.org/3/library/datetime.html. Last accessed 15th March 2021.

Regmi, S. (2020). Calculating the Square Root of a Number using the  Newton-Raphson Method [A How To Guide]. Available: https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo. Last accessed 15th March 2021.

Stojiljković, M. (2021). NumPy arange(): How to Use np.arange(). Available: https://realpython.com/how-to-use-numpy-arange/. Last accessed 15th March 2021.

Tutorials Point. (2021). Python - Command Line Arguments. Available: https://www.tutorialspoint.com/python/python_command_line_arguments.htm. Last accessed 17th March 2021.

W3Schools. (2021). Python slice() Function. Available: https://www.w3schools.com/python/ref_func_slice.asp. Last accessed 14th March 2021.
