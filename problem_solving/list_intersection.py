# Program to find the intersection of two lists
# Uses sets to find common elements

# Get input from the user
list1 = list(map(float, input("Enter first list numbers separated by spaces: ").split()))  # First list
list2 = list(map(float, input("Enter second list numbers separated by spaces: ").split()))  # Second list

# Find intersection using set
intersection = list(set(list1) & set(list2))

# Display the result
print(f"The intersection of the lists is: {intersection}")