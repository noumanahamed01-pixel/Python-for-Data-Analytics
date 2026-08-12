# Comprehensions are a concise way to create lists, sets, and dictionaries in Python, often replacing longer loops.

# List Comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print("Squares:", squares)

# With condition
evens = [x for x in numbers if x % 2 == 0]
print("Even Numbers:", evens)

# Nested comprehension
matrix = [[j for j in range(3)] for i in range(3)]
print("Matrix:", matrix)

# Dictionary Comprehension
marks = {"M": 85, "Alice": 90, "Bob": 78}
passed = {name: score for name, score in marks.items() if score >= 80}
print("Passed Students:", passed)

# Set Comprehension
unique_letters = {ch for ch in "hello world"}
print("Unique Letters:", unique_letters)



