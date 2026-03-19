# Write a program to prompt for a file name, and then read throught the file,
# and lookf for lines of the form: X-DSPAM-Confidence: 0.8475

# When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart
# the line to extract the floating-point number on the line.
# Count these lines and, then, compute the total of the span confidence values
# from these lines. When you reach the end of the file, print out the average
# spam confidence

fname = input('Enter a file name: ')

try:
    fhand = open(fname)
except:
    print('File cannot be opened', fname)
    exit()

count = 0
total = 0

for line in fhand:
    line = line.rstrip()
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    if line.startswith('X-DSPAM-Confidence:'):
        sp_pos = line.find(' ')
        str_num = line[sp_pos+1:]
        fl_num = float(str_num)
        count = count + 1
        total = total + fl_num
        average = total/count

print('Average spam confidence:', average)