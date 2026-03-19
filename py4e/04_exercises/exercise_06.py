# Rewrite your pay computation, with time-and-a-half for overtime, and create a function called `computepay`,
# which takes two parameters (`hours` and `rate`).

def computepay(hours, rate):
#    print("In computepay:", hours, rate)
    if hours > 40:
        base_pay = hours * rate
        overtime_pay = (hours - 40) * (rate * 0.5)
        total_pay = base_pay + overtime_pay
    else:
        total_pay = hours * rate
#    print("Returning", total_pay)
    return total_pay

input_hours = input("Enter Hours: ")    # user input hours

input_rate = input("Enter Rate: ")  # user input rate

float_hours = float(input_hours)    # converting user input hours to float data type

float_rate = float(input_rate)  # converting user input rate to float data type

xp = computepay(float_hours, float_rate)    # storage variable, which is assigned the return value for the call function

print("Pay:", round(xp, 2))