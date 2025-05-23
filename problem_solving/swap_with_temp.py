# Program to swap two variables using a temporary variable
# This program takes two numbers from the user and swaps their values

# Get input from the user
a = int(input("Enter the first number: "))  # First number input
b = int(input("Enter the second number: "))  # Second number input

# Display values before swapping
print(f"Before swapping: a = {a}, b = {b}")

# Swapping using a temporary variable
temp = a  # Store value of a in temp to avoid losing it
print(f"temp = {temp}")
a = b     # Assign value of b to a
print(f"a = {a}")
b = temp  # Assign temp (original a) to b
print(f"b = {b}")

# Display values after swapping
print(f"After swapping: a = {a}, b = {b}")