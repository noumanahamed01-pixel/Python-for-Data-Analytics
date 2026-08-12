# Importing the module
import mymodule

print(mymodule.greet("M"))
print("Sum:", mymodule.add(10, 20))
print("Value of PI:", mymodule.PI)

# Import specific functions
from mymodule import greet, add
print(greet("Alice"))
print("Sum:", add(5, 7))

# Import with alias
import mymodule as mm
print(mm.greet("Bob"))
