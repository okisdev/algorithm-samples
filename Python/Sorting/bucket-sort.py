
def insertion_sort_for_bucket(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def bucket_sort(arr):
    bucket = []
    slot_num = 10
    for i in range(slot_num):
        bucket.append([])

    for j in arr:
        index_b = int(slot_num * j)
        bucket[index_b].append(j)

    for i in range(slot_num):
        insertion_sort_for_bucket(bucket[i])

    k = 0
    for i in range(slot_num):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1
    return arr

# Testing
arr = [0.5, 0.4, 0.3, 0.2, 0.1]

print(bucket_sort(arr))  # [0.1, 0.2, 0.3, 0.4, 0.5]
