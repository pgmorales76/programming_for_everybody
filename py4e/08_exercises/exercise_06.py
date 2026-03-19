# Rewrite the program that prompts the user for a list
# of numbers, and prints out maximum, and minimum, of
# the numbers, at the end, when the user enters, "done".
# Write the program to store the numbers, the user enters,
# in a list, and use the `max()`, and `min()`, functions
# to compute the maximum, and minimum, numbers, after the
# loop completes.

numbers = []

while True :

    sval = input('Enter a number: ')

    if sval == 'done' :
        break

    try:
        fval = float(sval)

    except:
        print('Invalid input')
        continue

    numbers.append(fval)

print('Maximum:', max(numbers))
print('Minimum:', min(numbers))
