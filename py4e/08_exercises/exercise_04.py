# List all unique words, sorted in alphabetical order, stored in romeo.txt,
# containing a subset of Shakespeare's work.
# Write a program to open the file, romeo.txt, and read it, line by line.
# For each line, split the line into a list of words, using the `split` function.
# For each word, check to see if the word is, already, in the list of unique words.
# If the word isn't in the list of unique words, add it to the list.
# When the program completes, sort, and print, the list of unique words,
# in alphabetical order.

unique_words = []
file_input = input('Enter filename: ')
fhand = open(file_input)
for line in fhand:
    line = line.split()
    for word in line:
        if word not in unique_words:
            unique_words.append(word)

print(sorted(unique_words))
