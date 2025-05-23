# Program to find the union of two lists
# Uses sets to combine unique elements

# Get input from the user
list1 = list(map(float, input("Enter first list numbers separated by spaces: ").split()))  # First list
list2 = list(map(float, input("Enter second list numbers separated by spaces: ").split()))  # Second list

# Find union using set
union = list(set(list1) | set(list2))

# Display the result
print(f"The union of the lists is: {union}")