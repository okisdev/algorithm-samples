
def gnome_sort(arr):
    index = 0
    while index < len(arr):
        if index == 0 or arr[index - 1] <= arr[index]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
    return arr

# Testing
arr = [5, 4, 3, 2, 1]

print(gnome_sort(arr))  # [1, 2, 3, 4, 5]
