# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above forty hours.

hours = input("Enter Hours: ")

rate = input("Enter Rate: ")

gross_pay = float(hours) * float(rate)

# overtime pay forumla is to the left of the addition operator; base pay is to the right
if float(hours) > 40:
    gross_pay = (((float(hours) - 40) * float(rate) * 1.5) + (40 * float(rate)))

print("Pay:", round(gross_pay, 2))