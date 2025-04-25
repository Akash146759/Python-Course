def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Find middle index
        if arr[mid] == target:   # Found it!
            return mid
        elif arr[mid] < target:  # Search right half
            low = mid + 1
        else:                    # Search left half
            high = mid - 1

    return -1  # Not found

# Example sorted list
numbers = [1, 3, 5, 7, 9, 11, 13]

# Searching for 7
position = binary_search(numbers, 7)

if position != -1:
    print(f"Found at index {position}")  # Output: Found at index 3
else:
    print("Not found")
