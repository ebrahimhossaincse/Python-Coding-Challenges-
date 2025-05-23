# Program to print all prime numbers in a given interval
# Uses a function to check for prime numbers

# Function to check if a number is prime
def is_prime(n):
    if n < 2:  # Numbers less than 2 are not prime
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Check divisibility up to square root
        if n % i == 0:  # If divisible, not prime
            return False
    return True  # If no divisors found, it's prime

# Get input from the user
start = int(input("Enter the start of the interval: "))  # Start of range
end = int(input("Enter the end of the interval: "))  # End of range

# Print all prime numbers in the interval
print(f"Prime numbers between {start} and {end} are:")
for num in range(start, end+1):  # Loop through the range
    if is_prime(num):
        print(num, end=" ")  # Print prime numbers with a space
print()  # New line at the end