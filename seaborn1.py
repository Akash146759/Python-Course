import seaborn as sns
import matplotlib.pyplot as plt

# Subjects and number of students
subjects = ['Math', 'Science', 'English', 'History', 'Art']
votes = [3, 2, 1, 2, 2]

# Plotting
sns.barplot(x=subjects, y=votes)
plt.title('Favorite Subjects in Class 8')
plt.xlabel('Subjects')
plt.ylabel('Number of Students')
plt.show()
