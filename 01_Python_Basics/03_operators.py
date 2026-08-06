# Arithmetic → + - * / // % **
# Comparison → == != > < >= <=
# Logical → and, or, not
# Assignment → +=, -=, *=, /=
# Membership → in, not in
# Identity → is, is not

# Arithmetic Operators
a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# Comparison Operators
print("Is a equal to b?", a == b)
print("Is a not equal to b?", a != b)
print("Is a greater than b?", a > b)
print("Is a less than b?", a < b)
print("Is a greater or equal to b?", a >= b)
print("Is a less or equal to b?", a <= b)

# Logical Operators
x = True
y = False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

# Assignment Operators
num = 5
num += 2   # same as num = num + 2
print("After += :", num)
num *= 3   # same as num = num * 3
print("After *= :", num)

# Membership Operators
name = "Python"
print("'P' in name?", 'P' in name)
print("'z' not in name?", 'z' not in name)

# Identity Operators
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print("list1 is list2?", list1 is list2)   # False (different objects)
print("list1 is list3?", list1 is list3)   # True (same object)

#Write a program to take two numbers as input from the user and print their sum, difference, product, and quotient.
num1=int(input("Enter First Number:\n"))
num2=int(input("Enter Second Number:\n"))
print(f"Sum of {num1} and {num2} is: {num1+num2}")
print(f"Difference of {num1} and {num2} is: {num1-num2}")
print(f"Product of {num1} and {num2} is: {num1*num2}")
print(f"Quotient of {num1} and {num2} is: {num1/num2}")