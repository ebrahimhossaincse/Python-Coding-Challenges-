# Program to find the largest of three numbers
# Compares three numbers using the max() function

# Get input from the user
num1 = float(input("Enter the first number: "))  # First number input
num2 = float(input("Enter the second number: "))  # Second number input
num3 = float(input("Enter the third number: "))  # Third number input

# Find the largest number using max()
largest = max(num1, num2, num3)

# Display the result
print(f"The largest number is: {largest}")