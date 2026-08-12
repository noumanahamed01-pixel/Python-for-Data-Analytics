# Decorators are a powerful feature that let you add functionality to functions or classes without modifying their code directly.
# Decorator = function that takes another function as input and returns a new function.

# Syntax: @decorator_name above the target function.

# Useful for logging, authentication, timing, caching, validation.

# Keeps code clean and reusable.

# Basic decorator
def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, M!")

say_hello()

#Decorators with arguments
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

@log_decorator
def multiply(a, b):
    return a * b

add(10, 20)
multiply(5, 6)
