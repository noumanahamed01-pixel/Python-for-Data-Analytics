# Function definition
def greet(name):
    return f"Hello, {name}! Welcome to Python practice."

# Function with parameters and return value
def add_numbers(a, b):
    return a + b

# Function with default parameter
def introduce(name, course="BCA"):
    print(f"My name is {name}, and I study {course}.")

# Function calling
print(greet("M"))
print("Sum:", add_numbers(10, 5))
introduce("Alice")
introduce("Bob", "Data Science")

# PRACTICE PROGRAMS

# #write a program to create a function to print your name and age.
def name_and_age(name, age):
    print(f"Hello, Myself {name} and I am {age} years old.")
name=input("Enter your name: ")
age=int(input("Enter your age: "))
name_and_age(name, age)

# #write a program to create a function that greets the user with a message.
def greet_user(name):
    print(f"hello, {name}! Welcome to python programming.")
name=input("Enter your name:")
greet_user(name)

# #write a program to create a function to add  two numbers and return the result.
def add(num1, num2):
    return num1 + num2
num1=int(input("Enter the first number:\n"))
num2=int(input("Enter the second number:\n"))
result= add(num1, num2)
print(f"The sum of {num1} and {num2} is: {result}")

# #write a program to create a function to find square of a number and return the result.
def square(num):
    return num**2
num=int(input("Enter a number:\n"))
result=square(num)
print(f"The Square of {num} is: {result}")

# #write a program to create a function to check whether a given number is even or odd and return the result.
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = int(input("Enter a number: \n"))
result = check_even_odd(num)
print(f"The number is: {result}")

# #write a program to create a function to find area of rectangle and return the result.
def aor(length, breadth):
    return length * breadth
length=float(input("enter a length:"))
breadth=float(input("enter a breadth:"))
result= aor(length, breadth)
print(f"The Area of Rectangle: {result}")

# #write a porgram to create a function to find largest of two numbers.
def largest(num1,num2):
    if (num1>num2):
        return num1
    else:
        return num2
num1=int(input("enter a number1:"))
num2=int(input("Enter a number2:"))
result= largest(num1,num2)
if (result==num1):
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")

# #write a program to create a function to create student report card.
def src(name, age, marks):
    print("-------------------student_report_card-----------------------")
    print(f"name: {name}")
    print(f"Age: {age}")
    print(f"marks: {marks}")
    print("----------------------End of report--------------------------")
name=input("Enter your name:")
age=int(input("enter your age:"))
marks=int(input("enter your marks: "))
src(name, age, marks)

#write a program to find the sum of numbers from 1 to n
def sum(n):
    total_sum=0
    for i in range(1,n+1):
        total_sum+=i
        return total_sum
n=int(input("Enter a number:\n"))
result=sum(n)
print(f"The Sum of the first {n} natural number is {result}")
#without using function
n=int(input("Enter a number:"))
sum=0
for i in range(1,n+1):
    sum+=i
print("the sum of",n,"natural number is: ",sum)

# #write a program to find factorial of a given number.
def fact(n):
    fnum=1
    for i in range(1,n+1):
        fnum*=i
    print("The Factorial of ",n,"is ",fnum)
n=int(input("Enter a number:"))
fact(n)