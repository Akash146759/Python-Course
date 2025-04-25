import time

# Sample list of numbers
numbers = list(range(1, 10000))  # A list from 1 to 10,000

# Linear Search (O(n))
def linear_search(arr, target):
    for num in arr:
        if num == target:
            return True
    return False

# Binary Search (O(log n))
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

# Measure time for Linear Search
start_time = time.time()
linear_search(numbers, 9999)
end_time = time.time()
print(f"Linear search time: {end_time - start_time:.6f} seconds")

# Measure time for Binary Search
start_time = time.time()
binary_search(numbers, 9999)
end_time = time.time()
print(f"Binary search time: {end_time - start_time:.6f} seconds")
