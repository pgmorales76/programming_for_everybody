# Encapsulate this code in a function named `count`,
# and generalize it so that it accepts the string (word) and the letter as arguments.

# word = 'banana'

# count = 0

# for letter in word:
#     if letter == 'a':
#         count = count + 1

# print(count)

def count(word, letter):
    
    counter = 0

    for letter in word:
        if letter == 'a':
            counter += 1
    
    return counter

results = count('banana', 'a')

print(results)