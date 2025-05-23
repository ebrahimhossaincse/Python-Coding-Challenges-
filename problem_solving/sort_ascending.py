# Program to sort a list in ascending order
# Uses the sort() method

# Get input from the user
lst = list(map(float, input("Enter numbers separated by spaces: ").split()))  # List input

# Check if list is empty
if not lst:
    print("The list is empty")
else:
    # Sort the list in ascending order
    lst.sort()
    print(f"Sorted list in ascending order: {lst}")