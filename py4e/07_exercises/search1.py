# 7.5 - Searching through a file

fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:'):
        print(line)