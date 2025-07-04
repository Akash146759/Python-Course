import matplotlib.pyplot as plt

activities = ['Sleep', 'School', 'Play', 'Homework','rdundant']
hours = [8, 6, 4, 2, 5]

plt.pie(hours, labels=activities, autopct='%1.1f%%')
plt.title('Daily Time Spent')
plt.show()
