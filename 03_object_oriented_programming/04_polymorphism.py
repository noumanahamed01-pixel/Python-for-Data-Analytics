#Polymorsphism in Python,is the ability of a function or method to work in different ways based on the object that it is acting upon. 
#In Python, polymorphism allows us to define methods in the child class with the same name as defined in their parent class. This allows us to use a unified interface for different data types.

# 1_Method Overriding: This is a feature that allows a subclass or child class to provide a specific implementation of a method that is already defined in its superclass or parent class. The implementation in the subclass overrides (replaces) the implementation in the superclass.
# Base Class
class Animal:
    def speak(self):
        print("Animal makes a sound")

# Derived Classes override the method
class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Objects
animals = [Dog(), Cat(), Animal()]

for a in animals:
    a.speak()   # Same method name, different behavior

#2.method Overloading: Python does not support method overloading in the traditional sense, but we can achieve similar functionality using default arguments or variable-length arguments.
class MathOperations:
    def add(self, a, b=0, c=0):
        return a + b + c                                \

#3 built-in Polymorphism: Python's built-in functions like len(), str(), and print() are examples of polymorphism. They can operate on different data types, providing a unified interface for various objects.
# len() works differently depending on the object type
print(len("Python"))      # String → 6
print(len([1, 2, 3, 4]))  # List → 4
print(len({"a": 1, "b": 2}))  # Dictionary → 2

#4. Operator Overloading: Python allows us to define the behavior of operators for user-defined classes. This is another form of polymorphism where the same operator can have different meanings based on the context.
# + operator behaves differently
print(10 + 5)          # Addition → 15
print("Hello " + "M")  # String concatenation → Hello M
print([1, 2] + [3, 4]) # List concatenation → [1, 2, 3, 4]
