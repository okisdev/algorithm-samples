
def get_next_gap(gap):
    gap = (gap * 10) // 13
    if gap < 1:
        return 1
    return gap


def comb_sort(arr):
    n = len(arr)
    gap = n
    swapped = True
    while gap != 1 or swapped:
        gap = get_next_gap(gap)
        swapped = False
        for i in range(0, n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
    return arr

# Testing
arr = [5, 4, 3, 2, 1]

print(comb_sort(arr))  # [1, 2, 3, 4, 5]
