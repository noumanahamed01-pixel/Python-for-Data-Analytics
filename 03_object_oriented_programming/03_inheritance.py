# Base Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Derived Class (inherits from Person)
class Student(Person):
    def __init__(self, name, age, course):
        # Call base class constructor
        super().__init__(name, age)
        self.course = course
    
    def display_student(self):
        # Reuse base method + add new info
        self.display_info()
        print(f"Course: {self.course}")

# Another Derived Class
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def display_teacher(self):
        self.display_info()
        print(f"Subject: {self.subject}")

# Objects
student1 = Student("M", 21, "BCA")
teacher1 = Teacher("Alice", 35, "Data Science")

student1.display_student()
print("-----")
teacher1.display_teacher()
