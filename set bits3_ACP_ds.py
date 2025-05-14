def rightmost_set_bit(n):
    if n == 0:
        return 0  # No set bits in 0
    return n & -n  # Isolates the rightmost set bit

# Input from user
number = int(input("Enter a number: "))
result = rightmost_set_bit(number)
print("Rightmost set bit:", result)
