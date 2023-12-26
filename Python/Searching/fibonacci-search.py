
def fibonacci_search(arr, x):
    fib2 = 0
    fib1 = 1
    fibM = fib2 + fib1
    while fibM < len(arr):
        fib2 = fib1
        fib1 = fibM
        fibM = fib1 + fib2
    offset = -1
    while fibM > 1:
        i = min(offset + fib2, len(arr) - 1)
        if arr[i] < x:
            fibM = fib1
            fib1 = fib2
            fib2 = fibM - fib1
            offset = i
        elif arr[i] > x:
            fibM = fib2
            fib1 = fib1 - fib2
            fib2 = fibM - fib1
        else:
            return i
    if fib1 and arr[offset + 1] == x:
        return offset + 1
    return -1

# Testing
arr = [1, 2, 3, 4, 5]

print(fibonacci_search(arr, 3))  # 2
