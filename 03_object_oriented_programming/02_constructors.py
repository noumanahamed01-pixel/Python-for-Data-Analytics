# Constructor Example

class Student:
    # Constructor (__init__) is called automatically when object is created
    def __init__(self, name, course, year):
        self.name = name
        self.course = course
        self.year = year

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")
        print(f"Year: {self.year}")

# Creating objects (constructor runs automatically)
student1 = Student("M", "BCA", "Final")
student2 = Student("Alice", "Data Science", "Second")

student1.display_info()
print("-----")
student2.display_info()
