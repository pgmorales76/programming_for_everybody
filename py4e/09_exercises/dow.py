# Write a program that categorizes each mail message,
# by which day of the week the commit was done.
# To do this, look for lines that start with, "From",
# then, look for the third day, and keep a running
# count, of each, of the days of the week.
# At the end of the program, print out the contents,
# of your dictionary (order doesn't matter).)


fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

day_of_commit = dict()

for line in fhand:
    if line.startswith('From '):
        day_of_week = line.split()[2]
        day_of_commit[day_of_week] = day_of_commit.get(day_of_week, 0) + 1

print(day_of_commit)
