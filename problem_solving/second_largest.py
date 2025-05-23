# Program to find the second largest element in a list
# Sorts the list and picks the second element

# Get input from the user
lst = list(map(float, input("Enter numbers separated by spaces: ").split()))  # List input

# Check if list has at least 2 elements
if len(lst) < 2:
    print("List must have at least 2 elements")
else:
    lst.sort()
    print(f"Sorted list in ascending order: {lst}")
    print(f"The second largest element is: {lst[-2]}")

    # Sort in descending order and pick second element
    sorted_lst = sorted(lst, reverse=True)
    print(f"The second largest element is: {sorted_lst[1]}")