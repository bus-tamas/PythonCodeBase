def unique(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(unique(arr))

# Define a function that takes an array as an argument
def find_unique_number(arr):
    # Initialize the result to 0
    result = 0
    # Iterate over each bit position (0 to 31)
    for i in range(0, 32):
        # Initialize the sum of bits at the i-th position to 0
        sum = 0
        # Create a number with the i-th bit set
        x = (1 << i)
        # Iterate over each number in the array
        for j in range(0, len(arr)):
            # If the i-th bit is set in the j-th number, increment sum
            if arr[j] & x:
                sum += 1
        # If sum is not divisible by 3, set the i-th bit in result
        if (sum % 3):
            result |= x
    # Return the result, which is the number that appears once in the array
    return result

# Define the array to be passed to the function
arr = [6, 1, 3, 3, 3, 6, 6]
print(find_unique_number(arr))