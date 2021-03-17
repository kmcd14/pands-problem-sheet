# es.py
# This program reads in a text file and outputs the number of times 'e' appears.
# It will take a filename from an argument on the command line.
# Author: Katie Mc Donald

# Imports sys module
import sys

# Counter to keep track of the number of times 'e' appears
e_count = 0

# First argument is the script name so [1] is the next element
filename = sys.argv[1] # In this case the text file

# Opening the variable filename in read mode
with open(filename, 'r') as f:
    # Go through each line
     for line in f:
         # Getting rid of whitespace and making all letters lowercase so 'E' will be counted. 
         line = line.strip().lower()
         # Go through every letter in a line 
         for letter in line:
            if letter == 'e':
                e_count += 1 # Adds 1 to the counter total for each 'e' found
             
print(e_count)
