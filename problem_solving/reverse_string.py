# Program to reverse a string in multiple ways
# Shows three different methods to reverse a string

# Get input from the user
s = input("Enter a string to reverse: ")  # String input

# Method 1: Using slicing
reverse1 = s[::-1]  # Slicing with step -1 reverses the string
print(f"Reverse using slicing: {reverse1}")

# Method 2: Using reversed() function
reverse2 = "".join(reversed(s))  # Join characters from reversed iterator
print(f"Reverse using reversed(): {reverse2}")

# Method 3: Using a loop
reverse3 = ""  # Initialize empty string
for char in s:  # Iterate through each character
    reverse3 = char + reverse3  # Add character to the front
print(f"Reverse using loop: {reverse3}")