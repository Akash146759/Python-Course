def linear_search(arr, target):
    for i in range(len(arr)):  # Go through each item one by one
        if arr[i] == target:   # If we find it, return position
            return i
    return -1  # If not found, return -1

# Example list
numbers = [3, 7, 1, 9, 5]

# Searching for 9
position = linear_search(numbers, 5)

if position != -1:
    print(f"Found at index {position}")  # Output: Found at index 3
else:
    print("Not found")
