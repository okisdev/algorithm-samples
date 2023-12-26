
def binary_search(arr, x, start, end):
    if start == end:
        if arr[start] > x:
            return start
        else:
            return start + 1
    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < x:
        return binary_search(arr, x, mid + 1, end)
    elif arr[mid] > x:
        return binary_search(arr, x, start, mid - 1)
    else:
        return mid


def insertion_sort(arr):
    for i in range(1, len(arr)):
        x = arr[i]
        j = binary_search(arr, x, 0, i - 1)
        arr = arr[:j] + [x] + arr[j:i] + arr[i + 1:]
    return arr


def timsort(arr):
    runs, sorted_runs = [], []
    length = len(arr)
    new_run = [arr[0]]

    for i in range(1, length):
        if i == length - 1:
            new_run.append(arr[i])
            runs.append(new_run)
            break
        if arr[i] < arr[i - 1]:
            if not new_run:
                runs.append([arr[i - 1]])
                new_run.append(arr[i])
            else:
                runs.append(new_run)
                new_run = []
        else:
            new_run.append(arr[i])

    for each in runs:
        sorted_runs.append(insertion_sort(each))

    sorted_array = []
    for run in sorted_runs:
        sorted_array = merge(sorted_array, run)

    return sorted_array

# Testing
arr = [5, 4, 3, 2, 1]

print(timsort(arr))  # [1, 2, 3, 4, 5]
