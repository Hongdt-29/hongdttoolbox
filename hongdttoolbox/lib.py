def pushing_all_zeros_to_end_of_array(arr, n):
    count = 0 # Count of non-zero elements

    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count+=1
    while count < n:
        arr[count] = 0
        count += 1
    return arr
