
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[int(index % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val / exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr

# Testing
arr = [5, 4, 3, 2, 1]

print(radix_sort(arr))  # [1, 2, 3, 4, 5]
