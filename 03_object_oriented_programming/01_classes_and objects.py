# OOP Basics: Classes and Objects

# Defining a class
class Student:
    # Constructor (initializer)
    def __init__(self, name, course, year):
        self.name = name
        self.course = course
        self.year = year

    # Method to display student info
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")
        print(f"Year: {self.year}")

# Creating objects (instances of class)
student1 = Student("M", "BCA", "Final")
student2 = Student("Alice", "Data Science", "Second")

# Calling methods
student1.display_info()
print("-----")
student2.display_info()
