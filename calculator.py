#!/usr/bin/env python3
# Created By: Yoma Ozoh
# Date: November, 2025
# This program changes grade level to percentage
def calculate(sign, first_number, second_number):
    if sign == "+":
        return first_number + second_number
    elif sign == "-":
        return first_number - second_number
    elif sign == "%":
        return first_number % second_number
    elif sign == "/":
        return first_number / second_number
    elif sign == "*":
        return first_number * second_number


def main():
    # Loop until valid input is entered
    while True:
        # Ask the user to enter an operation
        sign = input("Please enter an operation (+, -, *, /, %): ")
        # Check if the operation is valid
        if sign != "+" and sign != "-" and sign != "*" and sign != "/" and sign != "%":
            print(sign, "isn't a valid operation. Please try again.\n")
            continue

        try:
            # Ask the user to enter first number
            first_number = float(input("Enter first number: "))
        # Catch errors if the input is not a number
        except ValueError:
            print(first_number, "is not a valid input. Please enter a valid input.\n")
            continue
        try:
            # ask the user for second number
            second_number = float(input("Enter second number: "))
        # Catch errors if the input is not a number
        except ValueError:
            print(second_number, "is not a valid input. Please enter a valid input.\n")
            continue

        # No dividing by zero
        if sign == "/" and second_number == 0:
            print("Error: You can't divide by 0. \n")
            continue

        # Call calculate function and store as result
        result = calculate(sign, first_number, second_number)

        # Display the result to user
        print("\nThe Results of:", first_number, sign, second_number, "is =", result)
        break


# Call the main function to start the program
if __name__ == "__main__":
    main()
