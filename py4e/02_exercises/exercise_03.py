# Write a program, to prompt the user for hours, and rate/hour, to compute gross pay.

hours = input("Enter Hours: ")

rate = input("Enter Rate: ")

gross_pay = float(hours) * float(rate)
    
print("Pay:", round(gross_pay, 2))  # The comma, inside the parentheses, effectively, creates a space.