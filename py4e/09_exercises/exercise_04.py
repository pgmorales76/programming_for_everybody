# Add code, to the program, in exercise_03.py, to
# figure out who has the most messages in the file.
# After all the data has been read, and the dictionary
# has been created, look through the dictionary using
# a maximum loop, to find who has the most messages
# and print how many messages the person has.

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

email_address = dict()
most_frequent_email_address = None
number_of_emails = 0

for line in fhand:
    if line.startswith('From '):
        email = line.split()[1]
        email_address[email] = email_address.get(email, 0) + 1

for itervar in email_address:
    if email_address[itervar] > number_of_emails :
        most_frequent_email_address = itervar
        number_of_emails = email_address[itervar]

print(most_frequent_email_address, number_of_emails)
