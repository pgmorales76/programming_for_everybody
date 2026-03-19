# Wrtie a program to read through the mail box data,
# and when you find the line that starts with, "From",
# you'll split the line, into words, using the `split`
# function.
# We're interested in who sent the message, which is the
# second word, on the "From" line.
# You'll parse the "From" line, and print out the second
# word, for each "From" line, then you'll, also, count
# the number of "From" lines, and print out a count, at
# the end.

file_input = input('Enter filename: ')
count = 0
fhand = open(file_input)
for line in fhand:
    if line.startswith('From '):
        print(line.split()[1])
        count += 1

print('There were', count, 'lines in the file with From as the first word')
