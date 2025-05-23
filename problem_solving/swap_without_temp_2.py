# Program to swap two variables without using a temporary variable
# Uses arithmetic operations to swap values

# Get input from the user
a = int(input("Enter the first number: "))  # First number input
b = int(input("Enter the second number: "))  # Second number input

# Display values before swapping
print(f"Before swapping: a = {a}, b = {b}")

a,b = b,a

# Display values after swapping
print(f"After swapping: a = {a}, b = {b}")