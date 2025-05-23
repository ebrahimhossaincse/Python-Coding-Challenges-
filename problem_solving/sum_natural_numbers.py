# Program to find the sum of first n natural numbers
# Uses the formula: sum = n * (n + 1) / 2

# Get input from the user
n = int(input("Enter a positive number (n) to sum up to: "))  # Number input

# Check if input is positive
if n <= 0:
    print("Please enter a positive number")
else:
    # Calculate sum using the formula
    sum_n = n * (n + 1) // 2  # Integer division for whole number result
    print(f"The sum of first {n} natural numbers is: {sum_n}")