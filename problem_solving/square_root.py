# Program to calculate the square root of a number
# Uses the math module for square root calculation

import math  # Import math module for sqrt() function

# Get input from the user
num = float(input("Enter a number to find its square root: "))  # Number input

# Check if the number is non-negative
if num < 0:
    print("Cannot calculate square root of a negative number")
else:
    sqrt = math.sqrt(num)  # Calculate square root
    print(f"The square root of {num} is: {sqrt}")