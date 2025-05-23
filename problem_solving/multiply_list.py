# Program to multiply all elements in a list
# Uses a loop to calculate the product

# Get input from the user
lst = list(map(float, input("Enter numbers separated by spaces: ").split()))  # List input

# Check if list is empty
if not lst:
    print("The list is empty")
else:
    # Calculate the product
    product = 1
    for num in lst:  # Multiply each number
        product *= num
    print(f"The product of elements is: {product}")