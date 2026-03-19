# Write a program that reads a file, and prints the letters,
# in decreasing order of frequency.
#
# Your program should convert all the input to lower-case,
# and only count the letters a-z. Your program shouldn't
# count spaces, digits, punctuation, or anything other than
# the letters a-z. Find text examples from several different
# languages and see how letter frequency varies between languages.
# Compare your results with the tables at https://en.wikipedia.org/wiki/Letter_frequency

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

letters = dict()

for line in fhand:
    line = line.rstrip()
    line = line.lower()
    words = line.split()
    for word in words:
        for character in word:
            if character not in alphabet:
                continue
            letters[character] = letters.get(character, 0) + 1

l = list()

for key, val in letters.items() :
    l.append((val, key))

l.sort(reverse=True)

for key, val in l:
    print(val, key)
