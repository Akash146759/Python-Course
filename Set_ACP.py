# Python program to find the symmetric difference between two sets

# Define two sample sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Method 1: Using the symmetric_difference() method
sym_diff_method = set1.symmetric_difference(set2)
print("Symmetric difference (using symmetric_difference method):", sym_diff_method)

# Method 2: Using the ^ operator
sym_diff_operator = set1 ^ set2
print("Symmetric difference (using ^ operator):", sym_diff_operator)
