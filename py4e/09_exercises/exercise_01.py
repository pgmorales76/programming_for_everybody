# Write a program that reads the words in `words.txt`,
# and stores them as keys, in a dictionary.
# It doesn't matter what the values are.
# Then, you can use the `in` operator, as a fast way to
# check whether a string is in a dictionary.

fname = input('Enter the file name: ')

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

words_dictionary = dict()

for line in fhand:
    keys = line.split()
    for key in keys:

        # using the `in` operator
        # if key not in words_dictionary:
        #     words_dictionary[key] = 1
        # else:
        #     words_dictionary[key] += 1

        # `get()` method
        words_dictionary[key] = words_dictionary.get(key, 0) + 1

print(words_dictionary)

lookup_key = input('Enter a word: ')

if lookup_key in words_dictionary:
    print('True')
else:
    print('False')
