# Program to remove duplicates from a list
# Uses a set to eliminate duplicates

# Get input from the user
lst = list(map(float, input("Enter numbers separated by spaces: ").split()))  # List input

# Check if list is empty
if not lst:
    print("The list is empty")
else:
    # Remove duplicates using set
    unique_lst = list(set(lst))
    print(f"List after removing duplicates: {unique_lst}")