# Generators are a simpler way to create iterators using the yield keyword. They let you produce values one at a time, without storing everything in memory.
# yield → pauses the function, returns a value, and resumes later.

# Generators are memory‑efficient (don’t store all values at once).

# Can be used in loops, pipelines, or with functions like next().

# Generator expressions → compact syntax, similar to list comprehensions but lazy.

# Simple generator function
def countdown(n):
    while n > 0:
        yield n   # yields one value at a time
        n -= 1

# Using the generator
for num in countdown(5):
    print(num)

# Generator for even numbers
def even_numbers(limit):
    for i in range(limit + 1):
        if i % 2 == 0:
            yield i

print("Even numbers up to 10:")
for e in even_numbers(10):
    print(e)

# Generator expression (short form, like list comprehension)
squares = (x**2 for x in range(1, 6))
print("Squares using generator expression:")
for s in squares:
    print(s)

