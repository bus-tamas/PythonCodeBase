



def maxsum(arr,n):
    max_sum = 0
    max_sum_subarray = []
    for i in range(len(arr) - (n-1)):
        current_sum = sum(arr[i:i+n])
        if current_sum > max_sum:
            max_sum = current_sum
            max_sum_subarray = arr[i:i+n]
    
    return max_sum_subarray

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        
print(maxsum(arr,3))

def max_sum_subarray(arr, window_size):
    """
    This function finds the maximum sum of a subarray of a given size.
    :param arr: The input array
    :param window_size: The size of the subarray
    :return: The maximum sum of a subarray of the given size
    """
    # Check if the array length is less than the window size
    if len(arr) < window_size:
        print("Invalid operation")
        return -1

    # Compute the sum of the first window
    window_sum = sum([arr[i] for i in range(window_size)])
    max_sum = window_sum

    # Compute sums of remaining windows by removing first element of the
    #  previous window and adding the last element of the current window
    for i in range(len(arr) - window_size):
        window_sum = window_sum - arr[i] + arr[i + window_size]
        max_sum = max(window_sum, max_sum)

    return max_sum

# Test the function
arr = [1, 9, -1, -2, 7, 3, -1, 2, 0, -2, 4]
window_size = 5
print(max_sum_subarray(arr, window_size))  # Output: 16