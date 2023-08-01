def bubble_sort(arr):
    for _ in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Testing
print(bubble_sort([5, 4, 3, 2, 1]))  # [1, 2, 3, 4, 5]
