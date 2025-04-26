class Student:
    # Constructor method
    def __init__(self, name, grade):
        self.name = name  # Assigning the name
        self.grade = grade  # Assigning the grade

    # Method to display student details
    def display_info(self):
        print("Name:", self.name)
        print("Grade:", self.grade)

# Creating an object of the Student class
student1 = Student("Akash", "7th Grade")
student2 = Student("Adithi", "8th Grade")

# Calling the method to display the student's information
student1.display_info()
student2.display_info()
