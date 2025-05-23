# Program to find the sum of elements in a list
# Uses the sum() function

# Get input from the user
lst = list(map(float, input("Enter numbers separated by spaces: ").split()))  # List input

# Check if list is empty
if not lst:
    print("The list is empty")
else:
    # Calculate the sum
    sum_lst = sum(lst)
    print(f"The sum of elements is: {sum_lst}")