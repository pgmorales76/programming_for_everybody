# This is Exercise 01, Chapter 07, pg. 89.
# Write a program to read through a file, and print the
# contents of the file (line by line), all in upper case.
# To get an idea of what the program should output, look to page 89.

fname = input('Enter a file name: ')

try:
    fhand = open(fname)
except:
    print('File cannot be opened', fname)
    exit()

for line in fhand:
    line = print(line.rstrip().upper())