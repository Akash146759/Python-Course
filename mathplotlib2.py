import matplotlib.pyplot as plt

fruits = ['Apple', 'Banana', 'Cherry', 'Grapes']
counts = [10, 15, 7, 12]

plt.bar(fruits, counts, color='purple')
plt.title('Fruit Count')
plt.xlabel('Fruit')
plt.ylabel('Count')
plt.show()
