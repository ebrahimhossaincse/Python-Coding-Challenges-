# Program to find the smallest element in a list
# Uses the min() function for simplicity

# Get input from the user
lst = list(map(float, input("Enter numbers separated by spaces: ").split()))  # List input

# Check if list is empty
if not lst:
    print("The list is empty")
else:
    # Find the smallest element
    smallest = min(lst)
    print(f"The smallest element is: {smallest}")