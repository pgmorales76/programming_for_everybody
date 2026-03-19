# Rewrite your pay program, using try and except, so that your program handles non-numeric input, gracefully, by printing a message, and exiting the program.

hours = input("Enter Hours: ")

try:
    int(hours)
except:
    print("Error, please enter numeric input")
    quit()

rate = input("Enter Rate: ")

try:
    gross_pay = float(hours) * float(rate)

    # overtime pay forumla is to the left of the addition operator; base pay is to the right
    if float(hours) > 40:
        gross_pay = (((float(hours) - 40) * float(rate) * 1.5) + (40 * float(rate)))

    print("Pay:", round(gross_pay, 2))
except:
    print("Error, please enter numeric input")
    quit()