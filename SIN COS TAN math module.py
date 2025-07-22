import math

# Input angle in degrees
angle_degrees = 45

# Convert to radians
angle_radians = math.radians(angle_degrees)

# Calculate sine, cosine, and tangent
sine = math.sin(angle_radians)
cosine = math.cos(angle_radians)
tangent = math.tan(angle_radians)

# Display the results
print(f"Sine({angle_degrees}°) = {sine}")
print(f"Cosine({angle_degrees}°) = {cosine}")
print(f"Tangent({angle_degrees}°) = {tangent}")
