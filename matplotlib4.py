import matplotlib.pyplot as plt

height = [120, 130, 125, 140, 135]
weight = [30, 35, 32, 40, 38]

plt.scatter(height, weight, color='red')
plt.title('Height vs Weight')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.grid(True)
plt.show()
