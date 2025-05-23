# Program to swap two variables without using a temporary variable
# Uses arithmetic operations to swap values

# Get input from the user
a = int(input("Enter the first number: "))  # First number input
b = int(input("Enter the second number: "))  # Second number input

# Display values before swapping
print(f"Before swapping: a = {a}, b = {b}")

# Swapping without a temporary variable
a = a + b  # Add a and b, store in a (e.g., a=5, b=10 -> a=15)
print(f"a = {a}") #15
b = a - b  # Subtract b from a, store in b (15-10=5 -> b=5)
print(f"b = {b}") #5
a = a - b  # Subtract new b from a, store in a (15-5=10 -> a=10)
print(f"a = {a}") #10

# Display values after swapping
print(f"After swapping: a = {a}, b = {b}")