def linear_search(arr, target):
    return arr.index(target) if target in arr else -1


# Testing
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5

result = linear_search(arr, target)

if result != -1:
    print("Element:{0} is present at index {1}".format(target, result))
else:
    print("Element:{0} is not present in array".format(target))
