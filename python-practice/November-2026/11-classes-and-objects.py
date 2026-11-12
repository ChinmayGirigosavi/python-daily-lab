# Topic: Classes & Objects in Python

# Note: External packages can be installed via terminal using 'pip'

class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

# Creating Student objects
student1 = Student("Jiya", "CS", 8.5, False)
student2 = Student("Chinmay", "CS", 8.5, False)

print(f"student1 name is {student1.name}, and student2 gpa is {student2.gpa}")