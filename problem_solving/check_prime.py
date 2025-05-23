# Program to check if a number is prime
# A prime number is greater than 1 and divisible only by 1 and itself
import math


# Function to check if a number is prime
def is_prime(n):
    if n < 2:  # Numbers less than 2 are not prime
        return False

    for i in range(2, int(math.sqrt(n))+1):  # Check divisibility up to square root
        print(f"value of i is {i}: ")
        print(f"value of n is {n}")
        if n % i == 0:  # If divisible, not prime
            return False
    return True  # If no divisors found, it's prime

# Get input from the user
num = int(input("Enter a number to check if it's prime: "))  # Number input

# Check and display result
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")