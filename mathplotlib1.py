import matplotlib.pyplot as plt

# Some marks scored by a student
subjects = ['Math', 'Science', 'English', 'History']
marks = [85, 90, 75, 80]

# Draw the graph
plt.plot(subjects, marks, marker='o', color='blue')
plt.title('Marks in Different Subjects')
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.grid(False)
plt.show()
