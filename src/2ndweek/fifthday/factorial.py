def num_of_factors(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count = count + 1
        else:
            continue
    return count

print(num_of_factors(10))
print(num_of_factors(100))
print(num_of_factors(101))
print(num_of_factors(17))


def num_of_factors2(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            count = count + 2
        if i * i == n:
            count = count - 1
        i += 1
    return count

print(num_of_factors2(10))
print(num_of_factors2(100))
print(num_of_factors2(101))
print(num_of_factors2(17))

def is_prime(n):
    if num_of_factors2(n) == 2:
        return True
    else:
        return False

print(is_prime(10))
print(is_prime(100))
print(is_prime(101))
print(is_prime(17))

import math

def halves(n):
    log_base_2 = math.log(n, 2)
    return math.floor(log_base_2)


print(halves(63))
print(halves(64))
print(halves(65))

def array_max_count(arr):
    max_item = max(arr)
    count = arr.count(max_item)
    return len(arr)-count

arr  = [10,20,30,30,30,10,20,10]

print(array_max_count(arr))


lst = [2, 5, 9, 11]
target = 20
for i in range(len(lst)-1):
    for j in range(i+1, len(lst)):
        if lst[i] + lst[j] == target:
            print(j, i)


def reverse(arr):
    i=0
    j = len(arr)-1
    cache = 0
    while i<j:
        cache = arr[i]
        arr[i] = arr[j]
        arr[j] = cache
        i += 1
        j -= 1
    return arr

print(reverse(arr))

print("Array ", arr)

def rotate_right(arr):
    last = arr[-1]
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1] 
    arr[0] = last
    return arr

print(rotate_right(arr))

def multiple_rotate_right(arr, n):
    for i in range(n):
        arr = rotate_right(arr)
    return arr

print(multiple_rotate_right(arr,3))

def reverse_array(arr, start, end):
    """
    This function reverses a portion of an array from index start to end.
    """
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array(arr, k):
    """
    This function rotates an array from right to left by k times.
    """
    n = len(arr)
    # Normalize the rotations if k is greater than array length
    k = k % n
    # Reverse the entire array
    reverse_array(arr, 0, n - 1)
    # Reverse the first 'k' elements
    reverse_array(arr, 0, k - 1)
    # Reverse the remaining 'n - k' elements
    reverse_array(arr, k, n - 1)

# Test the function
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate_array(arr, k)
print(arr)  # Output: [5, 6, 7, 1, 2, 3, 4]