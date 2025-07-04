def printPowerSet(set, set_size):
    power_set_size = 2**set_size  # Total subsets
    for outer in range(power_set_size):
        subset = []
        for inner in range(set_size):
            if (outer & (1 << inner)) > 0:
                subset.append(set[inner])
        print(subset)

# Example usage
arr = [1,2,3]
printPowerSet(arr, len(arr))
