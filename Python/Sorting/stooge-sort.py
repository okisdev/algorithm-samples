
def stooge_sort(arr, i=0, j=None):
    if j is None:
        j = len(arr) - 1
    if arr[j] < arr[i]:
        arr[i], arr[j] = arr[j], arr[i]
    if j - i + 1 > 2:
        t = (j - i + 1) // 3
        stooge_sort(arr, i, (j - t))
        stooge_sort(arr, i + t, (j))
        stooge_sort(arr, i, (j - t))
    return arr

# Testing
arr = [5, 4, 3, 2, 1]

print(stooge_sort(arr))  # [1, 2, 3, 4, 5]
