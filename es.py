# es.py
# This program reads in a text file and outputs the number of e's it contains.
# The program should take the filename from an argument on the command line.
# Author: Katie Mc Donald

e_count = 0

file_to_read = input('Enter the name of the file: ')
filename = file_to_read

with open(filename, 'r') as f:
     for line in f:
         # getting rid of whitespace + making all letters lowercase
         line = line.strip().lower()
         for word in line:
            if word == 'e':
             e_count += 1
             
print(e_count)
