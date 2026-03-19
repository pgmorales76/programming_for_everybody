# Write a program, which prompts the user, for a Celsius temperature, convert the temperature to Fahrenheit,
# and, print out, the, converted, temperature.

prompt = "Enter a temperature, in Celsius: "

celsius = input(prompt)

fahrenheit = ((float(celsius) * float(9/5)) + 32)

print(fahrenheit, 'Fahrenheit')