



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