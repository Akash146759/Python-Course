import matplotlib.pyplot as plt
import numpy as np
import math

# Let's analyze a logarithmic function: y = log(x)
# Create some x values (let's skip x=0 because log(0) is undefined)
x = np.linspace(0.1, 10, 100)  # Numbers between 0.1 and 10
y = np.log(x)  # Natural logarithm (base e)

# Plot the function
plt.plot(x, y, label="y = log(x)")

# Add labels and title
plt.title("Logarithmic Function")
plt.xlabel("x")
plt.ylabel("log(x)")
plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
plt.axvline(0, color="black", linewidth=0.5, linestyle="--")
plt.legend()

# Show the graph
plt.show()
