# Lambdas are anonymous functions (functions without a name) that are used for short, quick operations.
# Basic lambda function
square = lambda x: x * x
print("Square of 5:", square(5))

# Lambda with multiple arguments
add = lambda a, b: a + b
print("Sum:", add(10, 20))

# Lambda inside map()
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print("Squares:", squares)

# Lambda inside filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)

# Lambda inside sorted()
students = [("M", 85), ("Alice", 90), ("Bob", 78)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print("Sorted by Marks:", sorted_students)

# using opererator.add() more efiicient than lambda function
from functools import reduce
import operator
numbers = [1, 2, 3, 4, 5]
total_sum=reduce(operator.add,numbers)
print(total_sum)

