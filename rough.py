import matplotlib.pyplot as plt

# First plot in a 1 row x 2 column layout
plt.subplot(1, 2, 1)
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Plot 1")

# Second plot in the same layout
plt.subplot(1, 2, 2)
plt.plot([1, 2, 3], [6, 5, 4])
plt.title("Plot 2")

plt.suptitle("Using subplot()")
plt.show()
