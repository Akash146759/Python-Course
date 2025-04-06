import random

total_sum = 0

# Nested loop for dice rolls
for i in range(4):  # Outer loop (4 rows)
    for j in range(4):  # Inner loop (4 columns)
        roll = random.randint(1, 6)  # Simulate a dice roll (1 to 6)
        print(roll, end="\t")
        total_sum += roll
    print()  # Move to the next line

print(f"Total sum of dice rolls: {total_sum}")
