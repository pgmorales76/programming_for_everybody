# 8.1 - A list is a sequence

# cheeses = ['Cheddar', 'Edam', 'Gouda']

# numbers = [17, 123, 58, 99, 465]

# empty = []

# print(cheeses, numbers, empty)

# 8.2 - Lists are mutable

# print(cheeses[0])

# numbers[1] = 5
# The value of index '1' has been (re)assigned the value of '5'
# b/c the bracket operator appears on the left side of the assignment operator

# print(numbers)

# print(numbers[-1]) # 465

# print(numbers[-2]) # 99

# print(numbers[-3]) # 58

# The `in` operator, also, works, on lists
# Remember: `in` returns a Boolean value

# print('Edam' in cheeses)

# print('Brie' in cheeses)

# 8.3 - Traversing a list

# for cheese in cheeses:
#     print(cheese)

# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2 # multiplying an individual element, w/in the list
# print(numbers)

# for x in empty:
#     print('This never happens')
# print(x)    # You'll get a Traceback b/c `x` is undefined

# 8.4 - List operations

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)

# d = [0] * 4
# print(d)

# a_2 = a * 3
# print(a_2)

# 8.5 - List slices

# t = ['a', 'b', 'c', 'd', 'e', 'f']
# print(t[1:3])
# print(t[:4])
# print(t[3:])
# print(t[:])

# t[1:3] = ['x', 'y']
# print(t)

# 8.6 - List methods

# t = ['a', 'b', 'c']
# t.append('d')
# print(t)

# t1 = ['a', 'b', 'c']
# t2 = ['d', 'e']
# t1.extend(t2)
# print(t1)
# print(t2)

# t = ['d', 'c', 'e', 'b', 'a']
# t.sort()
# print(t)

# If you assign the value, of a list method,
# to a variable, you'll be disappointed, by the result,
# b/c most list methods are `void`; they modify the list,
# and return `None`

# 8.7 - Deleting elements

# t = ['a', 'b', 'c']
# x = t.pop(1)
# print(t)
# print(x)

# t = ['a', 'b', 'c']
# del t[1]
# print(t)

# t = ['a', 'b', 'c']
# t.remove('b')
# print(t)

# t = ['a', 'b', 'c', 'd', 'e', 'f']
# del t[1:5]
# print(t)

# 8.8 - Lists and functions

# nums = [3, 41, 12, 9, 74, 15]

# print(len(nums))
# print(max(nums))
# print(min(nums))
# print(sum(nums))
# print(sum(nums)//len(nums))

# 8.9 - Lists and strings

# s = 'spam'
# t = list(s)
# print(t)

# s = 'pining for the fjords'
# t = s.split()
# print(t)
# print(t[2])

# s = 'spam-spam-spam'
# delimiter = '-'
# t = s.split(delimiter)
# print(t)

# t = ['pining', 'for', 'the', 'fjords']
# delimiter = ' '
# s = delimiter.join(t)
# print(s)

# 8.10 - Parsing lines

# see search5.py
# that's the only bit of coding, in this section

# 8.11 - Objects and values

# a = 'banana'
# b = 'banana'
# c = a is b
# c = a == b
# print(c)
    
# a = [1, 2, 3]
# b = [1, 2, 3]

# c = a is b
# this'll evaluate to `false` b/c they're not identical

# c = a == b
# this'll evaluate to `true` b/c they're equivalent

# If two objects are identical, they're, also, equivalent
# If two objects are equivalent, they aren't, necessarily, identical

# print(c)

# 8.12 - Aliasing

# a = [1, 2, 3]
# b = a
# c = b is a
# print(c)

# b[0] = 17
# print(a)

# 8.13 - List arguments

# def delete_head(t):
#     del t[0]

# letters = ['a', 'b', 'c']

# delete_head(letters)

# print(letters)

# t1 = [1, 2]
# t2 = t1.append(3)
# print(t1)
# print(t2)

# t3 = t1 + [3]
# print(t3)
# new_list = t1 is t3
# print(new_list)

# def tail(t):
#     return t[-1:]

# letters = ['a', 'b', 'c']
# rest = tail(letters)
# print(rest)

# 8.14 - Debugging

# https://docs.python.org/3/library/stdtypes.html#common-sequence-operations

# https://www.w3schools.com/python/python_strings_methods.asp

# https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types

# https://www.w3schools.com/python/python_lists_methods.asp
