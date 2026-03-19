# Write a program, to look for lines of the form:
#     New Revision: 39772

# Extract the number, from each of the lines, using
# a regular expression, and the `findall()` method.

# Compute the average of the numbers, and print out
# the average as an integer.

import re

fname = input('Enter file:')

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

fhand = open(fname)

lst = list()

for line in fhand:
    line = line.rstrip()
    x = re.findall('^[A-Za-z]+\s[A-Za-z]+.\s([0-9]+)$', line)
    if len(x) > 0 :
        lst.append(int(x[0]))

print(int(sum(lst)/len(lst)))
