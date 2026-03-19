# This program counts the distribution of the hour, of the day,
# for each of the messages. You can pull the hour from the "From"
# line by finding the time string and, then, splitting that string
# into the parts using the colon character. Once you have accumulated
# the coutrs, for each hour, print out the counts, one per line, sorted
# by hour, as shown in the textbook (pg. 129).

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

time_stamp = dict()

for line in fhand:
    if line.startswith('From '):
        time_string = line.split()[5]
        hour_string = time_string.split(':')[0]
        time_stamp[hour_string] = time_stamp.get(hour_string, 0) + 1 


l = list()

for key, val in time_stamp.items() :
    l.append((key, val))

l.sort()

for key, val in l :
    print(key, val)
