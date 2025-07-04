import numpy as np

# Each row: [ID, Age, Height(cm)]
students = np.array([
    [1, 14, 160],
    [2, 13, 155],
    [3, 14, 158],
    [4, 15, 160],
    [5, 13, 150],
    [6, 14, 158],
    [7, 15, 162],
    [8, 13, 160],
    [9, 14, 155],
    [10, 15, 160]
])

# Sort by Height (index 2), then Age (index 1), then ID (index 0)
sorted_indices = np.lexsort((students[:, 1], students[:, 2]))
sorted_students = students[sorted_indices]

# Display the sorted result
print("ID  Age  Height")
print(sorted_students)
