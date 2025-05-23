# Program to sort a list in descending order
# Uses the sort() method with reverse=True

# Get input from the user
lst = list(map(float, input("Enter numbers separated by spaces: ").split()))  # List input

# Check if list is empty
if not lst:
    print("The list is empty")
else:
    # Sort the list in descending order
    lst.sort(reverse=True)
    print(f"Sorted list in descending order: {lst}")