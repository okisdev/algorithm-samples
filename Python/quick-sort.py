def quick_sort(arr, left, right):
    if left >= right:
        return arr

    i = left
    j = right
    standard = arr[left]

    while i != j:
        while arr[j] >= standard and i < j:
            j -= 1
        while arr[i] <= standard and i < j:
            i += 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[i] = arr[i], arr[left]

    quick_sort(arr, left, i - 1)
    quick_sort(arr, i + 1, right)

    return arr


# Testing
arr = [5, 4, 3, 2, 1]

print(quick_sort(arr, 0, len(arr) - 1))  # [1, 2, 3, 4, 5]
