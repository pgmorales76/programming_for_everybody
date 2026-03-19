# Revise a previous program (Exercise 4, Chapter 9), as follows:
# Read, and parse, the "From" lines, and pull out the addresses
# from the line. Count the number of messages from each person,
# using a dictionary.

# After all the data has been read, print the version with the
# most commits by creating a list of (count, email) tuples from
# the dictionary. Then, sort the list in reverse order, and
# print out the person who has the most commits.

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

email_address = dict()

for line in fhand:
    if line.startswith('From '):
        email = line.split()[1]
        email_address[email] = email_address.get(email, 0) + 1

l = list()

for key, val in email_address.items() :
    l.append((val, key))

l.sort(reverse=True)

for key, val in l[:1]:
    print(val, key)
