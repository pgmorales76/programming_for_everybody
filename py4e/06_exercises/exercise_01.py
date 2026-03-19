# Write a `while` loop that starts at the last character, in the string,
# and works its way backwards to the first character, in the string,
# printing each letter on a separate line, except backwards.

# This is the forward version
# fruit = 'banana'

# index = 0

# while index < len(fruit) :
#    letter = fruit[index]
#    print(letter)
#    index = index + 1

# This is the reverse version
# What this program does, essentially, is create a variable, and assign it a string value;
# set the string index to 0, uses `len` to return number of characters in the string;
# accesses the last character, in the string;
# makes equivalent the number of characters in the string, with the string indexes;
# then, increments, as it's stepping through the string, as it does in the forward version, above;
# When `index` is equal to the length of the string, the condition is false, and the body of the loop isn't executed.
# fruit = 'banana'

# index = 0   # This is going to treat the last character, in the string, as if it's the beginning

# length = len(fruit)     # This returns the number of characters, in the string (different than string indexes!)

# while index < len(fruit) :
#    last = fruit[length - 1]    # This accesses the last character, in the string
#    length = length - 1         # This makes equivalent the number of characters in the string, with the string indexes
#    # print("Length is; ", length)
#    print(last)
#    index = index + 1
#    # print("Index is: ", index)

# What's happening is the integer value, of `length`, is being decremented, while the integer value, of `index`, in being incremented.
# This is happening to create finality, in the while loop.

# Here is, yet another way of printing a string backwards: spell the word backwards, when creating the string variable!
# fruit = 'ananab'

# for banana in fruit:
#    print(banana)
