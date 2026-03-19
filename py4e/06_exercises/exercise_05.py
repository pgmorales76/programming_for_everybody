# Take the following Python code that stores a string:

str = 'X-DSPAM-Confidence: 0.8475'

# Use `find` and string slicing to extract the portion of the string after the colon character,
# and, then, use the `float` function to convert the extracted string into a floating point number.

sp_pos = str.find(' ')

#print(sp_pos)

str_num = str[sp_pos+1:]

#print(str_num)

#print(type(str_num))

fl_num = float(str_num)

#print(fl_num)

print(fl_num)