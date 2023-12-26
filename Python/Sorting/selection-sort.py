
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Testing
arr = [5, 4, 3, 2, 1]

print(selection_sort(arr))  # [1, 2, 3, 4, 5]
