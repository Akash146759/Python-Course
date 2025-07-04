import pandas as pd

# Create a magic notebook (DataFrame)
data = {
    'Name': ['Avi', 'Mira', 'Zara'],
    'Class': [6, 6, 6],
    'Marks': [85, 92, 78],
    'Fav_Subjects': [['Maths', 'English','CS'],['Maths', 'English','CS'],['Maths', 'English','CS']]
}

students = pd.DataFrame(data)
print(students)

topper = students[students['Marks'] == students['Marks'].mean()]
print(topper)


print(students['Fav_Subjects'].describe())

students['Section'] = ['B', 'A', 'C']
print(students)

sorted_students = students.sort_values(by='Section', ascending=True)
print(sorted_students)

students.to_csv("student_data2.csv", index=False)


