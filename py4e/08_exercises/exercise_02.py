# Figure out, which line of the above program, is, still, not properly guarded.
# See ff you an construct a text file, which cause the program to fail, and,
# then, modify the program, so that the line is properly guarded and test to
# make sure it handles your new text file.

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 : continue        # guardian code
    if words[0] != 'From': continue
    print(words[2])
