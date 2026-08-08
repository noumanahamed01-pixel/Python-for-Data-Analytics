# #class is a blueprint or template that defines the properties and behavior of objects

# #create a class student
class student:
   pass  #do nothing — it’s just a placeholder. So the class has no attributes or methods initially.
# #object is an instance of class, it contains actual data and can perform actions defines in the class.
# #create an object 
student1=student()
print(student)
# we can add attributes to the objects
student1.name='alice'
student1.age=20
print(student1.name)
print(student1.age)

class book:
    pass
book1=book()
book2=book()
book1.title='first time to practice oop'  
book1.author='numan'
#Even though the class didn’t define title or author, 
#Python lets you add attributes directly to an object.
#So now book1 has its own title and author
book2.title='second time to practice oop'
book2.author='numan'
print(book1.title)
print(book1.author)
print(book2.title)
print(book2.author)

# #constructor is a special method that runs automatically when obe=ject is created.
# #Create a class called Book.

# # Constructor should store: title,author,Create two books,Print both.
class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
book1=book("this is my first oop program",'alice')
print(book1.title)
print(book1.author)

#instance variable: the object's data
#instance methods: what the object can do with that data
class students:
    College_Student='ABC College'
    def __init__ (self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Name : ",self.name)
        print("Marks : ",self.marks)
    def get_avg(self):
        sum=0
        for i in self.marks:
            sum+=i
        print(f"hi {self.name},your avg score is: ",sum/3)
s1=students('karan',[88,54,34])
s2=students('alice',[87,98,77])
s1.display()
s2.display()
s1.name='jhon'  # we can change a attribute name directly.
s1.get_avg()
s2.get_avg()
print(students.College_Student)

# Encapsulation is method of wrapping data and methods into the single unit(Class) and restircting direct access to the personal data.
# The Data is accessed in the controlled ways using methods.

#types of access modifiers in python
# 1. public Member
class student:
    def __int__(self):
        self.name = 'Nouman'
s=student()
print(s.name)
# Accessible from anywhere

#2. Protected member
class Employee:
    def __init__(self):
        self._salary = 60000
    def show_salary(self):
        return self._salary
s1 = Employee()
#accessing using method 
print(s1.show_salary())
#direct access (possible, but not recommeneded)
print(s1._salary)

# #3. Private member
class Student:
    def __init__(self):
        self.__marks = 95

    def show_marks(self):
        return self.__marks
s1 = Student()
print(s1.show_marks())

#inheritance is the capacity odf one class to inherit properties and behavior from another class.
class Vehicle:
    def start(self):
        print("start the engine")
    def stop(self):
        print('stop the vehicle')
class car(Vehicle):
    def drive(self):
        print('drive with safely')
c=car()
c.start() # inherited from vehicle class
c.drive() # defined in class car
c.stop() # inherited from the vehicle class

# Polymorphism is the ability of the same method, function,
# or operator to perform different behaviors depending on the object or data it works with.
#                                 Polymorphism 
#                                      |
#   --------------------------------------------------------------------------------
#   |                                                                              |
#comile time polymorphism (method overloading)             Runtime polymorphism (method overriding)
# python doesn't support C-t polymorphism directly         # it support 
# Method overriding 
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):   # Dog inherits Animal
    def sound(self):  # Overriding
        print("Dog barks")

dog = Dog()
dog.sound()
# Dog replaces (overrides) the sound() method of Animal.
#  This is Method Overriding.


# Abstraction is the process of hiding the implementation details
# and showing only the essential features to the user.
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Dog barks")
dog = Dog()
dog.sound()