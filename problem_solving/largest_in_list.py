# Program to find the largest element in a list
# Uses the max() function for simplicity

# Get input from the user
lst = list(map(float, input("Enter numbers separated by spaces: ").split()))  # List input

# Check if list is empty
if not lst:
    print("The list is empty")
else:
    # Find the largest element
    largest = max(lst)
    print(f"The largest element is: {largest}")