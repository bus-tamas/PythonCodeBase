def max_product(arr):
    """
    This function finds the highest product possible by multiplying 3 numbers from an array.
    """
    # Initialize the three largest numbers and two smallest numbers
    max1 = max2 = max3 = float('-inf')
    min1 = min2 = float('inf')

    # Iterate over the array
    for num in arr:
        # Update the three largest numbers
        if num > max1:
            max3 = max2
            max2 = max1
            max1 = num
        elif num > max2:
            max3 = max2
            max2 = num
        elif num > max3:
            max3 = num

        # Update the two smallest numbers
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    # Return the maximum product of three numbers
    return max(max1 * max2 * max3, max1 * min1 * min2)

# Test the function
arr = [1, -10, -10, 1, 3, 2]
print(max_product(arr))  # Output: 300