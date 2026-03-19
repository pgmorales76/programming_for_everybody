# Write a program to read through a mail log;
# build a histogram, using a dictionary, to
# count how many messages have come from each
# email address; and, print the dictionary.

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

print(email_address)
