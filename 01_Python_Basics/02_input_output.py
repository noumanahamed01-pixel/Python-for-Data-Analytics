# Input and Output Practice

# Taking input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
course = input("Enter your course: ")

# Output using print
print("Hello,", name)
print("You are", age, "years old and studying", course)

# Output using f-string (cleaner way)
print(f"Welcome {name}! You are {age} years old and enrolled in {course}.")

name="Nouman"
age=20
print("Hello, Myself",name,"! Welcome To Python Training Session")
print(f"You are {age} years old.")
print("Hello, Myself {}! Welcome To Python Training Session".format(name))
print("You are {} years old.".format(age))

# #write a program to take a name, age from the user and print a message using f-string and format method.
name=input("enter the name:\n")
age=int(input("Enter the age:\n"))
print(f" Hello, Myself {name}! Welcome to Python Practce session.\n I am {age} Years Old.")