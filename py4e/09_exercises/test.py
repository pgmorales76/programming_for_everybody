# Chapter 9 - Dictionaries

# eng2sp = dict()
# print(eng2sp)

# eng2sp['one'] = 'uno'
# print(eng2sp)

# eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
# print(eng2sp)

# print(eng2sp['two'])

# print(len(eng2sp))

# print('one' in eng2sp)

# print('uno' in eng2sp)

# vals = list(eng2sp.values())
# print('uno' in vals)
# print(vals)
#________________________________________

# 9.1 - Dictionary, as a set of counters

# ______________________________________

# using `for` and `in` operator

# word = 'brontosaurus'
# d = dict()

# for c in word:
#     if c not in d:
#         d[c] = 1
#     else:
#         d[c] = d[c] + 1

# print(d)
#________________________________________________

# counts = {'chuck': 1, 'annie': 42, 'jan': 100}
# print(counts.get('jan', 0))
# print(counts.get('tim', 0))
# counts['lex'] = 69
# print(counts)
#________________________________________________

# using `get`

# word = 'brontosaurus'
# d = dict()

# for c in word:
#     d[c] = d.get(c, 0) + 1

# print(d)
#________________________________________________

# 9.2 - Dictionaries and files

# Look at count1.py, for this section's relevant code
#_____________________________________________________

# 9.3 - Looping and dictionaries

# counts = { 'chuck' : 1, 'annie' : 42, 'jan' : 100}
# for key in counts:
#     print(key, counts[key])
#_____________________________________________________

# counts = { 'chuck' : 1, 'annie' : 42, 'jan' : 100}
# for key in counts:
#     if counts[key] > 10:
#         print(key, counts[key])
#_____________________________________________________

# counts = { 'chuck' : 1, 'annie' : 42, 'jan' : 100}
# lst = list(counts.keys())
# print(lst)
# lst.sort()
# print(lst)
# for key in lst:
#     print(key, counts[key])
#_____________________________________________________

# 9.4 - Advanced text parsing

# Look at count2.py, for this section's relevant code
#_____________________________________________________
