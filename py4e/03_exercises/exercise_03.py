# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade, using the table from the textbook.

prompt = input("Enter score: ")

try:

    if float(prompt) > 0.0 and float(prompt) < 1.0:
        if float(prompt) >= 0.9:
            print("A")
    
        elif float(prompt) >= 0.8:
            print("B")
 
        elif float(prompt) >= 0.7:
            print("C")

        elif float(prompt) >= 0.6:
            print("D")

        elif float(prompt) < 0.6:
            print("F")

    else:
        print("Bad score")

except:
    print("Bad score")