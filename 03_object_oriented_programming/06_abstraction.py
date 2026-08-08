# Abstraction is about hiding implementation details and showing only the essential features. 
# In Python, abstraction is often implemented using abstract classes and abstract methods (via the abc module).

# Abstract Class → cannot be instantiated directly.

# Abstract Method → declared but not implemented in the base class.

# Child Classes → must implement all abstract methods.

# Ensures a common interface across different classes.

from abc import ABC, abstractmethod

# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass   # abstract method (must be implemented in child class)

    @abstractmethod
    def perimeter(self):
        pass

# Derived Class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Derived Class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Objects
shapes = [Circle(5), Rectangle(4, 6)]

for s in shapes:
    print("Area:", s.area())
    print("Perimeter:", s.perimeter())
    print("-----")
