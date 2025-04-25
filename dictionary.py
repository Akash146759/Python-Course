student_data = {
    'id1':
    {'name':['Sara'],
    'class': ['V'],
    'subject_integration': ['english, maths, science']
    },
    'id2':
    {'name':['David'],
    'class': ['V'],
    'subject_integration': ['english, maths, science']
    },
    'id3':
    {'name':['Sara'],
    'class': ['V'],
    'subject_integration': ['english, maths, science']
    },
     'id4':
    {'name':['Mehtej'],
    'class': ['V'],
    'subject_integration': ['english, maths, science']
    },
    }
    
# Loop through the dictionary
for student_id, details in student_data.items():
    print(f"Student ID: {student_id}")
    print(f"Name: {details['name'][0]}")
    print(f"Class: {details['class'][0]}")
    print(f"Subjects: {details['subject_integration'][0]}")
    print("-" * 30)  # Just a separator for better readability

#print('no. 1', student_data["id1"])
#print('no. 2', student_data["id2"])

#x = student_data.values()
#print(x)