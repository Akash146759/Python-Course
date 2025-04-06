import math

# Copy positive sign from 5 to -3
result1 = math.copysign(-3, 5)
print("Result 1:", result1)  # Output: 3.0

# Copy negative sign from -8 to 4
result2 = math.copysign(4, -8)
print("Result 2:", result2)  # Output: -4.0

# Edge case: zero
result3 = math.copysign(0, -5)
print("Result 3:", result3)  # Output: -0.0 (negative zero)
