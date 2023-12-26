
def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    i = 0
    for num in range(max_val + 1):
        for _ in range(count[num]):
            arr[i] = num
            i += 1
    return arr

# Testing
arr = [5, 4, 3, 2, 1]

print(counting_sort(arr))  # [1, 2, 3, 4, 5]
