# Chapter 10 - Tuples

# 10.1 - Tuples are immutable

# t = ('a', 'b', 'c', 'd', 'e')
# print(t)
# print(type(t))
# _____________________________

# t_01 = ('a',)
# print(t_01)
# print(type(t_01))
# _____________________________

# t_02 = ('a')
# print(t_02)
# print(type(t_02))
# _____________________________

# t = tuple()
# print(t)
# print(type(t))
# _____________________________

# t = tuple('lupins')
# print(t)
# _____________________________

# t = ('a', 'b', 'c', 'd', 'e')
# print(t[0])
# print(t[1:3])
# t[0] = 'A' => will give a TypeError
# t = ('A',) + t[1:]
# print(t)
# t = ('A',) + t[0:]
# print(t)
# t = ('A',) + t[:]
# print(t)
# ____________________________

# 10.2 - Comparing tuples

# t_a = (0, 1, 2) < (0, 3, 4)
# print(t_a)

# For the rest of this section's
# material, look at soft.py
# ________________________

# 10.3 - Tuple assignment

# m = ('have', 'fun')
# print(type(m))
# x, y = m
# print(x)
# print(y)
# print(m)
# _________________________

# m = ['have', 'fun']
# print(type(m))
# x, y = m
# print(x)
# print(y)
# print(m)
# _________________________

# m = ('have', 'fun')
# x = m[0]
# y = m[1]
# print(x)
# print(y)
# _________________________

# m = dict()
# m['have'] = 1
# m['fun'] = 2
# print(m)
# x = m[0]
# y = m[1]
# print(x, y)
# _________________________

# m = ['have', 'fun']
# print(type(m))
# (x, y) = m
# print(x)
# print(y)
# print(m)
# _________________________

# a, b = 0, 1
# print(a, b)
# a, b = b, a
# print(a, b)
# print(b, a)
# _________________________

# a, b = 1, 2, 3
# print(a, b)
# _________________________

# addr = 'monty@python.org'
# uname, domain = addr.split('@')
# print(uname)
# print(domain)
# _______________________________

# 10.4 - Dictionaries and tuples

# d = {'b': 1, 'a': 10, 'c': 22}
# t = list(d.items())
# print(t)
# print(t[0])
# _______________________________

# d = {'b': 1, 'a': 10, 'c': 22}
# t = list(d.items())
# print(t)
# print(t[0])

# t.sort()

# print(t)
# print(t[0])
# _______________________________

# 10.5 - Multiple assignment with dictionaries

# d = {'a': 10, 'b': 1, 'c': 22}
# for key, val in d.items() :
#     print(val, key)
#______________________________________________

# d = {'a': 10, 'b': 1, 'c': 22}
# l = list()
# for key, val in d.items() :
#     l.append((val, key))

# print(l)

# l.sort(reverse=True)

# print(l)
# _____________________________________________

# 10.6 - The most common words

# The code, for this section, may be found in
# count3.py, in this folder
# _____________________________

# 10.7 - Using tuples, as keys, in dictionaries

# directory = dict()
# last = 'Garet'
# first = 'Peter'
# number = '(555) 555-5555'
# directory[last, first] = number
# print(directory)

# for last, first in directory:
#     print(first, last, directory[last, first])

# _____________________________________________

# 10.8 - Sequences: strings, lists, and tuples - Oh, My!

# No code to be tested, here. Refer to textbook

# _______________________________________________________

# 10.9 - List comprehension

# list_of_ints_in_strings = ['42', '65', '12']
# list_of_ints = list()
# for x in list_of_ints_in_strings :
#     list_of_ints.append(int(x))

# print(sum(list_of_ints))
#___________________________________________

# list_of_ints_in_strings = ['42', '65', '12']
# list_of_ints = list(int(x) for x in list_of_ints_in_strings)

# print(sum(list_of_ints))
