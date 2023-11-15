def arr_compare(arr,x):
    count = 0
    for i in range(len(arr)):
        if arr[i] > x :
            arr[i] = -1
            count = count + 1
    return count


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(arr_compare(arr,5))