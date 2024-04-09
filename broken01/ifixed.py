#!/usr/bin/env python3
# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.

calc1 = 0.0
calc2 = 0.0
operation = ""

while calc1 != "q":
    calc1 = input("\nWhat is the first operator? Or, enter q to quit:")

    try:
        calc1 = float(calc1)
        if isinstance(calc1, float):
            print("First operator = " + str(calc1))

    except ValueError:
        calc1 = calc1.lower()

        if calc1 == "q":
            break
        else:
            print("Please give a valid numeric value.")
            continue

    calc2 = input("\nWhat is the second operator? Or, enter q to quit: ")

    try:
        calc2 = float(calc2)
        if isinstance(calc2, float):
            print("Second operator = " + str(calc2))

    except ValueError:
        calc2 = calc2.lower()

        if calc2 == "q":
            break
        else:
            print("Please give a valid numeric value.")
            continue
    
    operation = input("Enter an operation to perform on the two operators (+ or -): ")

    if operation == "+":
        print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))
    elif operation == '-':
        print("\n" + str(calc1) + " - " + str(calc2) + " = " + str(calc1 - calc2))
    else:
        print("\n Not a valid entry. Restarting...")
