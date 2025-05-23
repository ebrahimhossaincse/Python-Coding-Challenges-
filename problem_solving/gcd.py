# Program to find the Greatest Common Divisor (GCD) of two numbers
# Uses the Euclidean algorithm

# Function to calculate GCD
def gcd(a, b):
    while b:  # Continue until b becomes 0
        a, b = b, a % b  # Update a to b, b to remainder of a/b
    return a  # a is the GCD

# Get input from the user
num1 = int(input("Enter the first number: "))  # First number input
num2 = int(input("Enter the second number: "))  # Second number input

# Calculate and display GCD
result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")
