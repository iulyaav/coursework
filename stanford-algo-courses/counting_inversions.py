def count_inversions(arr, n, c):
    """It piggy-backs on the idea of merge sort."""
    if n <= 1:
        return arr, c

    mid = n // 2
    first_half, c_left = count_inversions(arr[:mid], mid, c)
    second_half, c_right = count_inversions(arr[mid:], mid, c)

    print("DEBUG: c={}, c_left={}, c_right={}".format(c, c_left, c_right))
    print("DEBUG: fist={}, second={}".format(first_half, second_half))
    c += (c_left + c_right)
    sorted_arr = []
    i = j = 0

    while i < mid and j < n - mid:
        if first_half[i] < second_half[j]:
            sorted_arr.append(first_half[i])
            i += 1
        else:
            sorted_arr.append(second_half[j])
            c += mid - i  # append inversion counter
            j += 1
    if i < mid:
        sorted_arr += first_half[i:]
    if j < n - mid:
        sorted_arr += second_half[j:]

    return sorted_arr, c



arr1 = [2, 1, 3, 4, 5]
print(count_inversions(arr1, len(arr1), 0))
print("----")
arr2 = [1, 3, 5, 2, 4, 6]
print(count_inversions(arr2, len(arr2), 0))
