import math

# 1. Using mathematical constants
print("Value of pi:", math.pi)
print("Value of e:", math.e)

# 2. Calculating square root
print("Square root of 16:", math.sqrt(16))

# 3. Finding GCD (Greatest Common Divisor)
print("GCD of 48 and 18:", math.gcd(48, 18))

# 4. Calculating power
print("2 raised to the power of 3:", math.pow(2, 3))

# 5. Rounding up or down
print("Ceiling of 4.2:", math.ceil(4.2))
print("Floor of 4.8:", math.floor(4.8))

# 6. Factorial of a number
print("Factorial of 5:", math.factorial(5))

# 7. Checking NaN or infinity
print("Is NaN:", math.isnan(float('nan')))
print("Is infinity:", math.isinf(float('inf')))

# Ensure all values are positive before passing to a function
values = [-4, -9, -16]
positive_values = [math.copysign(abs(num), 1) for num in values]
print("All positive values:", positive_values)  # Output: [4.0, 9.0, 16.0]

